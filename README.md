# 🌐 Domain Lookup App

A full-stack web application for querying domain registration information using the [WhoisXML API](https://whois.whoisxmlapi.com/). It provides both **domain information** and **contact information** for a given domain name.


---

## ✨ Features

- 🔍 Lookup domain or contact information
- 📋 Displays info in a readable tabular format
- 🎨 Interactive UI built with React
- 🔧 Backend in Python (Flask)
- 🌐 WHOIS API integration
- 📁 Fully functional local setup (frontend + backend)

---

## 🔧 Technologies

- **Frontend**: React
- **Backend**: Flask (Python)
- **API**: WhoisXML API
- **Styling**: Custom CSS
- **Version Control**: Git, GitHub

---

## 📁 Project Structure

domain-lookup-app/
│
├── backend/ # Flask backend
│ ├── app.py # Main backend logic
│ ├── .env # API key stored here (do NOT commit)
│ ├── requirements.txt # Python dependencies
│ └── ...
│
├── frontend/ # React frontend
│ ├── public/
│ ├── src/
│ ├── App.js
│ ├── App.css
│ └── ...
│
└── README.md

---

## 🚀 Getting Started

### 📦 Prerequisites

- Node.js and npm
- Python 3.9+
- A WhoisXML API key (free tier available)

---


## 📂 Setup

### ⚙️ Backend

1. **Navigate to Backend Folder**:
cd backend

2. **Create a Virtual Environment**:
python3 -m venv venv

source venv/bin/activate  # for macOS/Linux

venv\Scripts\activate     # for Windows

4. **Install Dependencies**:
pip install -r requirements.txt


5. **Add API Key to .env**:
WHOIS_API_KEY=your_api_key

6. **Run the Server**:
flask run

### 💻 Frontend

1. **Navigate to Frontend Folder**:
cd frontend

2. **Install Dependencies**:
npm install

3. **Start the React App**:
npm start



### API Endpoint:
POST http://127.0.0.1:5000/api/whois


### 📝 Deployment:

Run the backend (flask run).

Run the frontend (npm start).

Visit the app in your browser at http://localhost:3000.


### 🔒 Security & Privacy
API key is stored securely using .env.

.env is listed in .gitignore to prevent accidental uploads to GitHub.

No sensitive user data is collected or stored.



### 🚫 .gitignore setup

#### Python
__pycache__/
venv/
.env

#### Node
node_modules/
build/
.DS_Store


Author 👩‍💻 

Kanchan Chowdhary

📧 kanchan.chowdhary95@gmail.com


## 📜 License
This project is for educational use only.
---

This version includes all essential information but is more **concise** and focuses on what the user needs to know quickly. Let me know if you want to make further adjustments!

## 🙌 Acknowledgements

WhoisXML API

React Documentation

Flask Documentation


