# 🛒 ZenithBazaar – Flask Market Website

ZenithBazaar is a full-stack web application built with **Flask**, allowing users to register, log in, buy/sell items, and view their dashboard.  
This project was built as part of my **University Web Design Course** final project.

---

## 🚀 Features
- ✅ Home, About, Contact Us, Privacy Policy, Terms of Service pages
- ✅ Login & Register (with Flask-WTF validation)
- ✅ Bootstrap carousel image slider
- ✅ Font Awesome icons
- ✅ Buy/Sell items with modals
- ✅ Flask flash notifications (converted to Bootstrap Toasts)
- ✅ Dashboard to view users, products, and total balance
- ✅ Responsive design (Flexbox + Grid + Media Queries)

---

## 🗂 Project Structure
```

Market/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── video/
├── templates/
│   ├── include/
│   ├── home.html
│   ├── market.html
│   └── ...
├── models.py
├── routes.py
├── form.py
├── **init**.py
└── run.py

````

---

## 🛠 Tech Stack
- **Backend:** Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF
- **Frontend:** HTML, CSS, Bootstrap, FontAwesome, JS
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## ⚙️ Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ZenithBazaar.git
   cd ZenithBazaar
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python run.py
   ```

5. Visit the site in your browser:

   ```
   http://127.0.0.1:5000
   ```

---
