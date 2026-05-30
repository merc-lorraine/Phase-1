# Week 4: Fortifying the Node

## Overview

Week 4 focused on infrastructure hardening across virtual machines, containers, and network environments. Through hands-on labs, I learned how to isolate systems, secure containerized applications, and design segmented network architectures. The week emphasized building hardened environments that reduce attack surfaces and support secure application deployment.

## Skills Developed

* Virtualization concepts and hypervisors
* VirtualBox network configuration
* Host-Only, NAT, and Bridged networking
* Sandbox environment creation
* Docker container deployment and management
* Container lifecycle automation
* Docker Compose orchestration
* Multi-container application deployment
* Network segmentation and isolation
* Infrastructure hardening and security validation

## Labs Completed

### Day 1: The Ghost in the Machine

Configured a forensic sandbox environment using virtual machine isolation techniques. Modified network settings to create an air-gapped environment, validated isolation, and documented malware detonation test results.

**Artifact:** `sandbox_report.txt`

### Day 2: The Container Revolution

Deployed and managed Docker containers while learning the differences between virtual machines and containers. Automated the deployment, modification, auditing, and removal of an Nginx web server using a shell script.

**Artifact:** `deploy_web.sh`

### Day 3: The Conductor and the Fleet

Built and orchestrated a multi-container WordPress and database environment using Docker Compose. Implemented segmented FrontEnd and BackEnd networks to isolate the database from external access.

**Artifact:** `docker-compose.yml`

### Day 4: Hybrid Infrastructure Hardening Challenge

Designed and deployed a hardened hybrid environment consisting of virtual machines and containerized services. Verified network segmentation, removed unauthorized containers, validated isolation controls, and generated a machine-readable infrastructure audit report.

**Artifact:** `hyperstack_audit.json`

## Key Takeaways

This week expanded my understanding of infrastructure security by demonstrating how virtualization, containerization, and network segmentation work together to protect systems. Through practical deployment and hardening exercises, I gained experience building isolated environments, automating infrastructure management, and implementing defense-in-depth principles across modern computing environments.
