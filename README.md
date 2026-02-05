# 🛡️ Ransomware Detection and Simulation Project

A cybersecurity project that simulates ransomware behavior in a controlled sandbox environment and detects suspicious file activity in real time using Python.

---

## 📌 Project Overview

This project demonstrates how ransomware encrypts files and how such activity can be detected by monitoring abnormal file system behavior.

It is designed strictly for **educational and security research purposes** and runs safely inside a sandbox directory.

---

## 🎯 Objectives

- Simulate ransomware encryption and decryption safely  
- Monitor file system activity in real time  
- Detect ransomware-like behavior  
- Understand cryptography and malware detection concepts  
- Build practical cybersecurity skills  

---

## 🛠️ Technologies Used

- Python  
- Cryptography (Fernet)  
- Watchdog (File System Monitoring)  
- OS & Time Modules  
- Visual Studio Code  

---

## 📂 Project Structure

RansomwareProject/
│
├── Sandbox/ # Folder monitored for ransomware activity
│ ├── test1.txt
│ ├── test2.txt
│ └── notes.txt
│
├── create_key.py # Generates encryption key
├── ransomware_simulator.py # Encrypts files (simulates ransomware)
├── decryptor.py # Decrypts encrypted files
├── detector.py # Detects suspicious file changes
├── thekey.key # Encryption key file
└── README.md


---

## ⚙️ How It Works

### 1️⃣ Key Generation
- A secure encryption key is generated using the Cryptography library.
- The key is stored in `thekey.key`.

### 2️⃣ Ransomware Simulation
- Files inside the `Sandbox` folder are encrypted.
- File extensions are modified.
- Ransomware-like behavior is simulated safely.

### 3️⃣ Decryption
- Encrypted files are restored using the same key.
- Original content is recovered.

### 4️⃣ Real-Time Detection
- Watchdog monitors file system activity.
- Detects rapid and abnormal file changes.
- Raises an alert when suspicious behavior is found.

---

## ▶️ How to Run the Project

Step 1: Install Dependencies
pip install cryptography watchdog
Step 2: Generate Encryption Key
python create_key.py
Step 3: Start the Detector
python detector.py
Step 4: Run Ransomware Simulator
python ransomware_simulator.py
Step 5: Decrypt Files
python decryptor.py
🚨 Sample Output
--- Starting Real-Time Detector on folder: 'Sandbox' ---

!!! WARNING: RANSOMWARE-LIKE ACTIVITY DETECTED !!!
Detected multiple file changes in the last few seconds.
🔐 Security Concepts Used
Symmetric Key Encryption

File System Monitoring

Behavioral Malware Detection

Sandbox Testing

Threat Simulation

📚 Learning Outcomes
Understood ransomware encryption mechanisms

Learned to use the Python Cryptography library

Implemented real-time file monitoring

Gained experience in malware detection logic

Built a real-world inspired cybersecurity project

⚠️ Disclaimer
This project is created strictly for educational purposes.

It does NOT perform real malicious activities and must NOT be used to harm systems, networks, or users.

The author is not responsible for any misuse of this project.