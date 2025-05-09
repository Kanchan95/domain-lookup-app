# Domain Lookup App

A full-stack web application for querying domain registration information using the [WhoisXML API](https://whois.whoisxmlapi.com/). It provides both **domain information** and **contact information** for a given domain name.

---

## Features

- **Domain Info**: Displays details like domain name, registrar, registration date, and hostnames.
- **Contact Info**: Provides registrant, admin, and technical contact details.
- **Interactive UI**: Users can select between domain or contact info, with a responsive design.
- **Loading State**: Displays a loader while fetching data.

---

## Technologies

- **Frontend**: React
- **Backend**: Flask (Python)
- **API**: WhoisXML API
- **Styling**: Custom CSS
- **Version Control**: Git, GitHub

---

## Setup

### Backend

1. **Navigate to Backend Folder**:
cd backend

2. **Create a Virtual Environment**:
python3 -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate     # for Windows

3. **Install Dependencies**:
pip install -r requirements.txt


4. **Add API Key to .env**:
WHOIS_API_KEY=your_api_key

5. **Run the Server**:
flask run

### Frontend

1. **Navigate to Frontend Folder**:
cd frontend

2. **Install Dependencies**:
npm install

3. **Start the React App**:
npm start



### API Endpoint:
POST http://127.0.0.1:5000/api/whois


### Deployment:

Run the backend (flask run).
Run the frontend (npm start).
Visit the app in your browser at http://localhost:3000.



### .gitignore

# Python
__pycache__/
venv/
.env

# Node
node_modules/
build/
.DS_Store


Author
Kanchan Chowdhary
📧 kanchan.chowdhary95@gmail.com


---

This version includes all essential information but is more **concise** and focuses on what the user needs to know quickly. Let me know if you want to make further adjustments!


