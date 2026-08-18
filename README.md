# Cyber Summer Fundamentals - Week 1 System Auditor

## Project Goal
To establish a baseline developer environment, learn core terminal navigation, and deploy a Python script that gathers host system metrics for basic IT asset auditing.

## Tech Stack
* **Operating System:** Windows 11
* **IDE:** Visual Studio Code
* **Language:** Python 3.x
* **Version Control:** Git & GitHub

## Repository Structure
```text
cyber-summer-fundamentals/
├── README.md
├── scripts/
│   └── system_auditor.py
└── screenshots/
    ├── vscode_setup.png
    ├── git_verify.png
    └── python_output.png

## Week 2: Network Traffic & Protocol Analysis

### Captured File: `captures/ping_dns_baseline.pcapng`

#### Diagnostic Test
* **Command Executed:** `ping google.com`
* **Filter Applied in Wireshark:** `icmp`

#### Header Data Summary
* **Layer 2 (Data Link):** MAC Addresses (Source Host MAC -> Local Router Gateway MAC)
* **Layer 3 (Network):** 
  * Source IP: `142.251.45.78`
  * Destination IP: `192.168.1.88`
* **Layer 4 (Transport):** ICMP Protocol (Echo Request Type 8 / Echo Reply Type 0)
* **DNS Resolution:** Captured initial domain name resolution on Port 53 (UDP) prior to ICMP ping echo.

### Key Learnings
* Verified the encapsulation process across the OSI model layers.
* Confirmed DNS translates human-readable hostnames (`google.com`) to Layer 3 IP addresses before establishing ICMP communication.