# 🛡️ Ransomware Simulation & Detection System

A cybersecurity project that simulates ransomware behavior in a controlled sandbox environment and detects suspicious file activity in real time using Python.

---

## 📌 Project Overview

This project demonstrates how ransomware encrypts files and how such behavior can be detected through real-time monitoring of file system activity.

It is designed strictly for **educational and security research purposes** and operates safely within a sandbox directory.

---

## 🎯 Objectives

- Simulate ransomware encryption and decryption safely  
- Monitor file system activity in real time  
- Detect ransomware-like behavior  
- Understand cryptography and malware detection concepts  
- Build practical cybersecurity skills  

---

## 🛠️ Tech Stack

- Python  
- Cryptography (Fernet)  
- Watchdog (File System Monitoring)  
- OS & Time Modules  

---

## 📂 Project Structure
RansomwareProject/
│
├── Sandbox/
│ ├── test1.txt
│ ├── test2.txt
│ └── notes.txt
│
├── create_key.py
├── ransomware_simulator.py
├── decryptor.py
├── detector.py
├── thekey.key
└── README.md
---

## ⚙️ How It Works

### 🔑 Key Generation
- Generates a secure encryption key using Fernet  
- Stores the key in `thekey.key`

### 🔐 Ransomware Simulation
- Encrypts files inside the `Sandbox` folder  
- Simulates ransomware-like behavior safely  

### 🔓 Decryption
- Uses the same key to restore original files  

### 🚨 Real-Time Detection
- Monitors file system using Watchdog  
- Detects rapid and abnormal file changes  
- Triggers alerts for suspicious activity  

---

## ▶️ How to Run

### Install dependencies
```bash
pip install cryptography watchdog
Generate key
python create_key.py
Start detection system
python detector.py
Run ransomware simulation
python ransomware_simulator.py
Decrypt files
python decryptor.py
```

🚨 Sample Output
--- Starting Real-Time Detector on folder: 'Sandbox' ---

!!! WARNING: RANSOMWARE-LIKE ACTIVITY DETECTED !!!
Detected multiple file changes in the last few seconds.

🔐 Security Concepts Covered
Symmetric Key Encryption
File System Monitoring
Behavioral Malware Detection
Sandbox Testing
Threat Simulation

📚 Learning Outcomes
Understood ransomware encryption mechanisms
Implemented real-time file monitoring
Applied cryptography using Python
Designed malware detection logic
Built a real-world cybersecurity simulation project
