# 👋 Hello Render App

A simple **Streamlit** application deployed on **Render** 🌐.  
This project demonstrates how to deploy a Python web app easily and for free.

🔗 **Live App:** https://render-test-1-gqrv.onrender.com

---

## 🚀 Features
- 🧠 Built with **Python + Streamlit**
- 🌈 Interactive web interface
- ☁️ Hosted on **Render** (free tier)
- ⚙️ Auto-updates when you push new commits to GitHub

---

## 🛠️ Installation (Run locally)

1. **Clone the repository**
   
   git clone https://github.com/HadilBoussensla/Render-test-.git
   cd Render-test-
   

Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py

📂 Project Structure

project/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Dependencies
├── render.yaml          # Render deployment config
└── README.md


☁️ Deployment on Render
Go to https://render.com

Connect your GitHub account

Click New → Web Service

Select your repository

Set:

Build Command → pip install -r requirements.txt

Start Command → streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

Click Create Web Service

🎉 That’s it! Your app is live at:
👉 https://hello-render.onrender.com

👩‍💻 Author
Created by Hadil Boussensla 💫

