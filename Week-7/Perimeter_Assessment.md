# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 ([172.88.0.28]):** 
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.66 ((Debian))
443/tcp  open  ssl/http Apache httpd 2.4.66 ((Debian))
8443/tcp open  ssl/http nginx
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

* **Host 2 ([172.88.0.44]):**
PORT     STATE SERVICE   VERSION
80/tcp   open  http      BusyBox httpd 1.13
554/tcp  open  rtsp      DoorBird video doorbell rtspd
8000/tcp open  http-alt?
Service Info: OS: Linux; Device: webcam; CPE: cpe:/o:linux:linux_kernel

* **Host 3 ([172.88.0.191]):**
PORT      STATE    SERVICE   VERSION
80/tcp    open     http
110/tcp   filtered pop3
111/tcp   filtered rpcbind
443/tcp   open     ssl/https
10001/tcp open     http      lighttpd
10002/tcp open     http      lighttpd
10003/tcp open     http      lighttpd
10004/tcp open     http      lighttpd
2 services unrecognized despite returning data.

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** [172.88.0.28: + The anti-clickjacking X-Frame-Options header is not present.+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST ]
* **Web Server 2 Finding:** [172.88.0.28: + The anti-clickjacking X-Frame-Options header is not present.]

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** [Apache HTTP 2.4.66]
* **Justification:** [As per NIST, CVE-2026-24072, there is an escalation of privilege bug in various midules of Apache HTTP 2.4.66. The product does not properly assign, modify, track, or check privileges for an actor, creating an unintended sphere fo control for a threat actor. Vulnerable to attack patterns of privilege abuse, privilege escalation and restful privilege eevation. This CVE record is still currently being enriched.]

