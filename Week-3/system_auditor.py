#!/usr/bin/env python3
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
# YOUR CODE HERE:
result = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# INSTRUCTION 2: Search the captured output for the malicious process
# YOUR CODE HERE:
found = False
for line in result.stdout.splitlines():
    if "unauthorized_cryptominer" in line:
        found = True
        print(f"Found it: {line}")
        alert_data = {"event": "Unauthorized Process", "severity": "High", "process": "unauthorized_cryptominer"}
        with open("security_alert.json", "w") as f:
                json.dump(alert_data, f, indent=4)
if not found:
    print("Audit Complete: No unauthorized processes detected.")
# INSTRUCTION 3: If found, create a dictionary and save it to 'security_alert.json'
# YOUR CODE HERE:  with open("security_alert.json", "w") as f: json.dump(alert_data, f, indent=4)

print("[+] Audit Complete.")
