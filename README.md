# 🛡️ Login Flooder Tool

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/GUI-Tkinter-yellow" alt="GUI">
  <br>
  A Python tool for simulating mass login requests on phishing pages (for authorized penetration testing).
</div>

---

## 📌 Table of Contents
- [✨ Features](#-features)
- [📸 Screenshots](#-screenshots)
- [⚙️ Prerequisites](#️-prerequisites)
- [🚀 Setup](#-setup)
- [🎯 Usage](#-usage)
- [⚠️ Ethics](#️-ethics)
- [📂 Code Structure](#-code-structure)
- [🔧 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features
- **GUI Interface** built with `tkinter`.
- **Multi-threaded requests** with advanced options:
  - **Tor support** for IP rotation.
  - Random credential generation (username/password).
  - User-Agent rotation.
- **Detailed logs** for success/failure tracking.

---

## 📸 Screenshots
<div align="center">
  <img src="sami_banner.png" alt="Tool Interface" width="600">
</div>

---

## ⚙️ Prerequisites
- **Python 3.6+**
- Install dependencies:
  ```bash
  pip install requests pillow stem tkinter
sudo apt install tor  # For Linux

🚀 Setup
Clone the repository:
git clone https://github.com/yourusername/login-flooder.git
cd login-flooder

Install libraries:
pip install -r requirements.txt

Run the tool:
python login_flooder.py

🎯 Usage
Enter the phishing page URL in the input field.
Set the number of requests to send.
Toggle Tor (if needed).
Click Start Attack to begin.
Monitor results in the log window.
⚠️ Ethics
⚠️ Use this tool only for legal purposes (e.g., testing your own systems).
🚫 Unauthorized use is strictly prohibited.


