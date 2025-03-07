# 🤖 Telegram Echo Bot

A simple **Telegram Echo Bot** built using the latest `python-telegram-bot` library. The bot repeats any message sent by the user.  

## 🚀 Features
✅ Simple and easy to use  
✅ Uses **async functions** for better performance  
✅ Built with the latest `python-telegram-bot` v20+  
✅ Works on **Linux, Windows, and MacOS**  
✅ Deployable on **Heroku, Railway, or VPS**  

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/NadirAliOfficial/telegram-echo-bot.git
cd telegram-echo-bot
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Get Your Telegram Bot Token
1. Open **Telegram** and search for `@BotFather`.
2. Send `/newbot` and follow the instructions.
3. Copy the **bot token** provided by BotFather.

---

## 🎯 Usage

### 1️⃣ Replace Your Bot Token
Open `echo_bot.py` and replace:
```python
TOKEN = "YOUR_BOT_TOKEN"
```

### 2️⃣ Run the Bot
```bash
python echo_bot.py
```

### 3️⃣ Test the Bot
1. Open Telegram and search for your bot.
2. Send any message, and the bot will **echo it back**!

---

## 🛠 Deployment

### **🔹 Deploy on Heroku**
1. Install the Heroku CLI:
   ```bash
   npm install -g heroku
   ```
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a Heroku app:
   ```bash
   heroku create your-echo-bot
   ```
4. Add a `Procfile`:
   ```plaintext
   worker: python echo_bot.py
   ```
5. Deploy:
   ```bash
   git add .
   git commit -m "Deploy Telegram Echo Bot"
   git push heroku main
   heroku ps:scale worker=1
   ```

### **🔹 Deploy on VPS**
1. Upload the script to your server.
2. Run the bot in a **tmux** or **screen** session:
   ```bash
   python echo_bot.py &
   ```

---

## 📜 Requirements.txt
If you need to create a `requirements.txt` file, use:
```bash
pip freeze > requirements.txt
```
Or manually add:
```plaintext
python-telegram-bot
```

---

## 📌 Contributing
Feel free to fork, improve, or add features to this bot. Pull requests are welcome! 🎉

---

## 📝 License
This project is **open-source** and available under the **MIT License**.

---

### ⭐ If you found this useful, please consider giving a star ⭐ to the repository!
```

---

### **🔥 What This README Includes**
✅ **Project description**  
✅ **Installation & setup instructions**  
✅ **How to run the bot**  
✅ **Deployment options (Heroku & VPS)**  
✅ **Requirements & dependencies**  
✅ **Contributing guidelines**  
✅ **License & credits**  

