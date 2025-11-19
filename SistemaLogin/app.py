from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "segredo_top"

# --- Cria tabela se não existir ---
def init_db():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()

init_db()

# --- Tela inicial (login) ---
@app.route("/")
def login():
    return render_template("login.html")

# --- Autenticação ---
@app.route("/login", methods=["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]

    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    
    user = cur.fetchone()
    con.close()

    if user and check_password_hash(user[2], password):
        session["user"] = email
        return redirect("/home")
    else:
        return "Email ou senha incorretos"

# --- Cadastro ---
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_user():
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])

    try:
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        con.commit()
        con.close()
        return redirect("/")
    except:
        return "Email já está em uso"

# --- Página protegida ---
@app.route("/home")
def home():
    if "user" in session:
        return f"Bem-vindo(a), {session['user']}!"
    return redirect("/")

app.run(debug=True)
