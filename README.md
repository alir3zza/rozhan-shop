# 🛍️ Rozhan — Django E-Commerce Website

Rozhan is a web-based e-commerce project developed with **Python and Django**.
The project provides the basic features of an online shopping platform, including user authentication, product management, and shopping cart functionality.

## 🚀 Features

* 👤 User registration and login
* 🔐 User authentication
* 🚪 User logout
* 👨‍💻 User profile
* 🛒 Shopping cart
* 📦 Product management
* 🔎 Product details
* 📄 Pagination
* 🛠️ Django Admin Panel
* 📱 Responsive web interface

## 🧰 Technologies

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **CSS**
* **Bootstrap**
* **Git & GitHub**

## 📁 Project Structure

```text
Rozhan/
│
├── account/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── product/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── contact/
│   ├── migrations/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── rozhan/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/rozhan.git
cd rozhan
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🔑 Create a Superuser

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then visit:

```text
http://127.0.0.1:8000/admin/
```

## 📸 Screenshots

Screenshots of the project can be added here.

```text
screenshots/
├── home.png
├── products.png
├── product-detail.png
├── login.png
└── register.png
```

## 🧑‍💻 Author

**Alireza Rahimi**

Electrical Engineering Student
Backend Developer | Python & Django

## 📌 Project Status

🚧 This project is currently under development.

More features and improvements will be added in future versions.

## 📄 License

This project is created for educational and development purposes.

