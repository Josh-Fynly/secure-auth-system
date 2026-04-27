# secure-auth-system
A defensive cybersecurity project implementing a secure authentication system with attack detection, rate limiting, and logging.


🔐 Secure Auth System (Defensive Cybersecurity Project)

📌 Overview

This project implements a secure authentication system designed to defend against common attacks such as:

- Brute force attacks
- Credential stuffing
- Account takeover

It includes:

- Password hashing (bcrypt)
- Rate limiting
- Account lockout
- JWT authentication
- Security logging (for SIEM integration)

---

🧠 Objectives

- Learn real-world authentication security
- Simulate attack scenarios
- Build a foundation for a Security Operations pipeline

---

🏗️ Architecture

User → API → Auth Logic → Database
↓
Security Layers
↓
Logs

---

⚙️ Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- bcrypt
- JWT (python-jose)

---

🚀 Getting Started

pip install -r requirements.txt
uvicorn app.main:app --reload

---

🔍 Features

- Secure password storage
- Login attempt tracking
- Account lock after failed attempts
- Rate limiting per IP
- Structured logging

---

📈 Future Enhancements

- SIEM integration
- Multi-factor authentication (MFA)
- Redis-based rate limiting
- Docker deployment

---

⚠️ Disclaimer

This project is for educational and defensive cybersecurity purposes only.
