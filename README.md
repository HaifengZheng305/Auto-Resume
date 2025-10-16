# 🧠 Auto Resume

**Tech Stack:** React, Next.js, Tailwind CSS, Node.js, Express, MongoDB, LangChain, REST API, Git  

Auto Resume is a full-stack web application that generates **tailored resumes** by aligning a user's professional experience with specific **job descriptions**. It leverages **AI (LangChain + GPT)** to create context-aware resume bullet points, helping users stand out in job applications.

---

## 🚀 Features

- **AI-Powered Resume Generation**  
  Utilizes **LangChain** and **GPT** to automatically craft personalized resume bullet points based on the user's experience and target job description.

- **Modern, Responsive UI**  
  Built with **React** and **Tailwind CSS** for a sleek, responsive, and user-friendly design that works across all devices.

- **Secure Authentication**  
  Includes **login**, **signup**, and **password reset** functionalities for a safe and personalized user experience.

- **Full-Stack Architecture**  
  Combines a **Next.js** front end with an **Express + MongoDB** backend for efficient data flow and dynamic content storage.

- **Data Persistence & API Integration**  
  Stores user profiles, resumes, and generated content securely using **MongoDB**, and integrates with a RESTful API for communication between the client and server.

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React, Next.js, Tailwind CSS |
| **Backend** | Node.js, Express.js |
| **Database** | MongoDB |
| **AI / NLP** | LangChain, GPT API |
| **Version Control** | Git, GitHub |
| **API** | REST API |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```Bash
git clone https://github.com/your-username/auto-resume.git
cd auto-resume
```
### 2. Install dependencies

```
cd frontend
npm install

cd ../backend
npm install
```
### 3. et up environment variables

```Create a .env file in the backend directory and include the following:
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
OPENAI_API_KEY=your_openai_api_key
```
###Run the development servers

```In two separate terminals:
cd frontend
npm run dev

# Backend
cd backend
npm start
```
The frontend will typically run at http://localhost:3000
and the backend at http://localhost:5000.
