# Week 11: The Fortress

## Overview

Week 11 focused on network defense, intrusion detection, endpoint monitoring, and defense-in-depth architecture. Building on knowledge gained throughout the program, I implemented multiple layers of security controls designed to prevent, detect, and respond to malicious activity. Through firewall engineering, IDS deployment, and endpoint detection configuration, I gained practical experience defending enterprise infrastructure against realistic attack scenarios.

## Skills Developed

* Network perimeter security
* UFW and iptables firewall management
* DMZ architecture design
* Egress filtering
* Network segmentation
* Intrusion Detection Systems (IDS)
* Suricata deployment and configuration
* Custom IDS signature development
* Network traffic analysis
* Endpoint Detection and Response (EDR)
* Sysmon for Linux monitoring
* Process creation auditing
* XML detection policy development
* Defense-in-depth architecture

## Labs Completed

### Day 1: The Barricade

Configured host-based firewall protections using UFW and implemented advanced iptables rules to restrict unauthorized communications and limit lateral movement between network segments.

**Artifact:** `firewall_config.sh`

### Day 2: The Tripwire

Deployed Suricata as a network intrusion detection system and developed custom detection signatures to identify reconnaissance activity and suspicious application-layer traffic.

**Artifact:** `custom_ids.rules`

### Day 3: The Last Mile

Implemented Sysmon for Linux to monitor endpoint activity, analyzed process creation events, and developed XML detection policies to identify suspicious behavior associated with ransomware activity.

**Artifact:** `edr_policy.xml`

### Day 4: Operation Fortress

Designed and validated a defense-in-depth architecture that combined firewall controls, intrusion detection signatures, and endpoint monitoring policies. Implemented multiple layers of protection to block, detect, and investigate simulated adversary activity across the network and host environments.

**Artifact:** `Operation_Fortress_Report.md`

## Key Takeaways

This week demonstrated how effective security requires multiple layers of defensive controls working together. By implementing firewall restrictions, custom intrusion detection signatures, and endpoint monitoring policies, I gained practical experience building a defense-in-depth strategy capable of preventing, detecting, and responding to threats throughout the attack lifecycle. Week 11 served as the culmination of Phase 1 by bringing together offensive security knowledge and defensive engineering practices into a unified security architecture.
