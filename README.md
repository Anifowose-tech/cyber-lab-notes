# Cyber Summer Fundamentals - System Auditor
## Week 2: Network Traffic & Protocol Analysis

### Captured File: `captures/ping_dns_baseline.pcapng`

#### Diagnostic Test
* **Command Executed:** `ping google.com`
* **Filter Applied in Wireshark:** `icmp`

#### Header Data Summary
* **Layer 2 (Data Link):** MAC Addresses (Source Host MAC -> Local Router Gateway MAC)
* **Layer 3 (Network):** 
  * Source IP: `192.168.1.88`
  * Destination IP: `142.251.211.110`
* **Layer 4 (Transport):** ICMP Protocol (Echo Request Type 8 / Echo Reply Type 0)
* **DNS Resolution:** Captured initial domain name resolution on Port 53 (UDP) prior to ICMP ping echo.

### Key Learnings
* Verified encapsulation process across the OSI model layers.
* Confirmed DNS translates human-readable hostnames (`google.com`) to Layer 3 IP addresses before establishing ICMP communication.

## Network Reconnaissance: Nmap Port Audit

### Target: scanme.nmap.org

| Port Number | Protocol | State | Service | Discovered Version |
| :--- | :--- | :--- | :--- | :--- |
| 22 | TCP | Open | SSH | OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0) |
| 80 | TCP | Open | HTTP | Apache httpd 2.4.7 ((Ubuntu)) |

### Takeaways
* **Port Discovery:** Identified active services exposed on public target infrastructure.
* **Banner Grabbing (`-sV`):** Extracted service versions necessary for patch management and threat analysis.

## Project Goal
To establish a baseline developer environment, learn core terminal navigation, and deploy a Python script that gathers host system metrics for basic IT asset auditing.

## Tech Stack
* **Operating System:** Windows 11
* **IDE:** Visual Studio Code
* **Language:** Python 3.x
* **Version Control:** Git & GitHub

## Repository Structure
```text
cyber-lab-notes/
├── README.md
├── captures/
│   └── ping_dns_baseline.pcapng
├── scans/
│   ├── scanme_basic.txt
│   └── scanme_services.txt
├── scripts/
│   └── system_auditor.py
└── screenshots/
    ├── vscode_setup.png
    ├── git_verify.png
    ├── python_output.png
    └── wireshark_icmp.png
