# 🛡️ Ransomware Detection and Simulation Project

A cybersecurity project that simulates ransomware behavior in a controlled sandbox environment and detects suspicious file activity in real time using Python.

---

## 📌 Project Overview

This project demonstrates how ransomware encrypts files and how such activity can be detected by monitoring abnormal file changes.  
It is built for **educational and security research purposes only** and runs safely inside a sandbox folder.

---

## 🎯 Objectives

- Simulate ransomware encryption and decryption safely  
- Monitor file system activity in real time  
- Detect ransomware-like behavior based on rapid file changes  
- Improve understanding of cryptography and malware detection concepts  

---

## 🛠️ Technologies Used

- **Python**
- **Cryptography (Fernet)**
- **Watchdog (File system monitoring)**
- **OS & Time modules**
- **VS Code**

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
├── ransomware_simulator.py# Encrypts files (simulates ransomware)
├── decryptor.py # Decrypts encrypted files
├── detector.py # Detects suspicious file changes
├── thekey.key # Encryption key file
└── README.md

---

## ⚙️ How It Works

### 1️⃣ Key Generation  
- A unique encryption key is generated using the Cryptography library  
- The key is saved in `thekey.key`

### 2️⃣ Ransomware Simulation  
- Files inside the Sandbox folder are encrypted  
- File extensions are changed  
- A ransom-like behavior is simulated  

### 3️⃣ Decryption  
- Encrypted files are restored using the same key  

### 4️⃣ Real-Time Detection  
- Watchdog monitors file changes  
- If many files change quickly, it raises an alert  
- Mimics ransomware behavior detection

---

## ▶️ How to Run the Project

### Step 1: Generate Key
```bash
python create_key.py

 Step 2: Start Detection

python detector.py

Step 3: Run Ransomware Simulator
python ransomware_simulator.py

Step 4: Decrypt Files
python decryptor.py

🚨 Sample Output
--- Starting Real-Time Detector on folder: 'Sandbox' ---
!!! WARNING: RANSOMWARE-LIKE ACTIVITY DETECTED !!!
Detected multiple file changes in the last few seconds.

🔐 Security Concepts Used

Symmetric key encryption

File system monitoring

Behavioral detection

Sandbox testing

Malware simulation

📚 Learning Outcomes

Understood ransomware encryption mechanisms
Learned to use Python Cryptography library
Implemented file system monitoring using Watchdog
Gained practical experience in malware detection logic
Built a real-world inspired cybersecurity project

⚠️ Disclaimer

This project is created strictly for educational purposes.
It does NOT perform real malicious actions and should NOT be used to harm systems.