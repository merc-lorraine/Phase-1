# Week 5: The Sovereign Domain

## Overview

Week 5 focused on Identity and Access Management (IAM) through the deployment and administration of a Windows Active Directory environment. Through hands-on labs, I learned how to build and manage a domain infrastructure, automate user provisioning, enforce security policies through Group Policy Objects (GPOs), and integrate Linux systems into a centralized identity framework. The week emphasized identity as the security perimeter and demonstrated how centralized governance enables secure enterprise operations.

## Skills Developed

* Windows Server administration
* Active Directory architecture
* Domain Controller deployment
* Organizational Unit (OU) management
* PowerShell automation
* User provisioning with New-ADUser
* Group Policy Object (GPO) deployment
* LSDOU inheritance model
* Policy enforcement and compliance auditing
* Linux Active Directory integration
* SSSD and realmd configuration
* Cross-platform identity management
* Enterprise access control

## Labs Completed

### Day 1: The Corporate Brain

Promoted a Windows Server to a Domain Controller, created an Active Directory forest and Organizational Unit structure, and automated user account provisioning using PowerShell scripts.

**Artifact:** `onboard_engineers.ps1`

### Day 2: The Invisible Hand

Created and deployed Group Policy Objects to enforce security controls across domain users. Audited policy inheritance, forced policy updates, and documented GPO enforcement procedures.

**Artifact:** `gpo_audit.txt`

### Day 3: Bridging the Kingdoms

Integrated an Ubuntu system with Active Directory using realmd and SSSD, enabling centralized authentication and administrative access across Windows and Linux environments.

**Artifact:** `unified_identity.png`

### Day 4: Operation Sovereign Domain

Completed a full-scale domain administration exercise by provisioning identities, deploying access control policies, validating Linux domain authentication, and generating compliance documentation.

**Artifacts:**

* `tlab5_report.txt`
* `unified_identity.png`

## Key Takeaways

This week demonstrated how identity serves as the foundation of enterprise security. By building an Active Directory environment, automating user management, enforcing policy through GPOs, and integrating Linux systems into the domain, I gained practical experience managing centralized authentication, authorization, and access control across a multi-platform enterprise environment.
