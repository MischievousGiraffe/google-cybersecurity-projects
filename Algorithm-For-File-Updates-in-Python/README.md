# Writing an Algorithm for File Updates in Python

## 📌 Project Overview
This project demonstrates the use of Python to automate access control management by updating an allow list of approved IP addresses. The scenario is based on a healthcare organization where protecting restricted content—such as patient records—is critical while maintaining availability for authorized users.

## 🎯 Objective
Create a Python algorithm that automatically updates an `allow_list.txt` file by removing IP addresses that appear in a separate `remove_list`, ensuring that only authorized devices retain access to restricted resources.

## 🏥 Scenario Context
As security professionals in a healthcare environment, it is essential to regulate access to sensitive information. Only devices from approved hospital networks or authorized VPN connections are permitted access.  

When a remote clinic or device loses authorization, its IP address is added to a removal list and must be promptly blocked to prevent unauthorized access.

## 🛠️ Tools & Technologies
- **Python** — File handling and algorithmic logic
- **Text Files (`.txt`)** — Storing allow and remove IP lists
- **Basic Automation Concepts** — Input validation and list updates

## 📁 Files Included
- `allow_list.txt` — List of IP addresses approved for access  
- `update_allow_list.py` — Python script that performs the update  
- `Algorithm for file updates in Python` — Project documentation  

## ⚙️ How the Algorithm Works
1. Reads the IP addresses from `allow_list.txt`
2. Reads the IP addresses from `remove_list`
3. Compares both lists
4. Removes any IP address from the allow list that appears in the remove list
5. Writes the updated allow list back to the file

## 🔐 Security Relevance
This project reflects a real-world access control scenario where automation reduces the risk of human error, ensures timely revocation of access, and supports compliance with healthcare security standards.

## 🧠 Key Skills Demonstrated
- Python file input/output (I/O)
- Algorithmic thinking
- Access control principles
- Secure handling of authorization data
- Practical automation in a security context

## 📎 Notes
All IP addresses and data used in this project are simulated for educational purposes only.
