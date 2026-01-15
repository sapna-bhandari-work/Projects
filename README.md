# Projects Repository

## Author
**Sapna Bhandari**  
Third Year B.Sc. Computer Engineering Student

---

## Repository Overview

This repository contains a collection of academic and self-driven projects focused on **Cybersecurity, Networking, Blockchain, Cryptocurrency, and Automation**.  
The projects are developed to gain practical exposure to real-world concepts such as ethical hacking, vulnerability assessment, web automation, decentralized systems, and sentiment-based trading.

All projects are educational in nature and implemented primarily using **Python**.

---

## Project Descriptions

---

## 1. MAC Address Changer

**Domain:** Cybersecurity / Networking

A Python-based tool that enables MAC address spoofing on Linux-based systems. The script allows users to specify a network interface and assign a new MAC address programmatically.

### Key Concepts
- MAC address spoofing
- Network interface control
- Command-line argument parsing

### Technologies Used
- Python
- subprocess, optparse, re
- Linux networking utilities

---

## 2. Vulnerability Scanner (Port Scanner with Banner Grabbing)

**Domain:** Cybersecurity

This project implements a multi-threaded port scanner that performs banner grabbing on open ports and compares the results against a list of known vulnerable service banners to detect potential security risks.

### Key Concepts
- Port scanning
- Banner grabbing
- Vulnerability identification
- Multithreading

### Technologies Used
- Python
- socket, IPy, threading
- Custom vulnerable banner database

---

## 3. Web Crawler

**Domain:** Web Automation / Security

A basic multithreaded web crawler that recursively visits internal links of a target website while avoiding duplicate URLs and external domains.

### Key Concepts
- Web crawling
- Queue-based task management
- HTML parsing

### Technologies Used
- Python
- urllib2, BeautifulSoup
- Queue, threading

---

## 4. Crypto Miner on WiFi Router (Duino-Coin Miner)

**Domain:** Blockchain / Cryptocurrency

A lightweight cryptocurrency miner designed to run on low-power WiFi routers using OpenWRT. The project demonstrates proof-of-work mining on constrained hardware.

### Key Concepts
- Proof-of-work mining
- Low-power blockchain computation
- Network communication

### Technologies Used
- Python
- hashlib, socket, requests
- OpenWRT environment

---

## 5. Reddit Sentiment-Based Crypto Trading Bot

**Domain:** Artificial Intelligence / Cryptocurrency Trading

An automated trading bot that analyzes Reddit posts for cryptocurrency-related discussions, performs sentiment analysis using NLP techniques, and places trades on Binance based on market sentiment.

### Key Concepts
- Sentiment analysis
- Automated trading
- API integration
- Natural language processing

### Technologies Used
- Python
- Reddit API (praw)
- Binance API
- NLTK (VADER Sentiment Analyzer)
- YAML and JSON configuration files

---

## Installation and Requirements

- Python 3.x
- Linux environment (recommended for cybersecurity tools)
- Required libraries are listed in `requirements.txt` where applicable
- API credentials are required for projects involving Reddit and Binance

---

## Disclaimer

All projects in this repository are intended strictly for **educational and learning purposes**.  
They have been tested in controlled environments such as virtual machines and test networks.

Any misuse of the code for unethical or illegal activities is not the responsibility of the author.

---

## Conclusion

This repository showcases practical implementations of core computer engineering concepts across multiple advanced domains.  
It reflects hands-on learning, experimentation, and a strong foundation in cybersecurity, automation, and blockchain technologies.
