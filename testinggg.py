from flask import Flask, redirect, request, render_template_string

app = Flask(__name__)

HTML_LOGIN = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StreamHub Login</title>
  <style>
    body {
      margin: 0;
      background: linear-gradient(135deg, #0b0b0b, #111827);
      color: white;
      font-family: Arial, sans-serif;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .card {
      width: 400px;
      background: rgba(25,25,25,0.95);
      border: 1px solid #333;
      border-radius: 14px;
      padding: 28px;
      box-shadow: 0 18px 40px rgba(0,0,0,0.5);
    }
    h2 {
      margin-top: 0;
      text-align: center;
      font-size: 36px;
      color: #e50914;
      margin-bottom: 20px;
    }
    input, button {
      width: 100%;
      box-sizing: border-box;
      padding: 14px;
      border-radius: 8px;
      border: none;
      margin-top: 12px;
      font-size: 16px;
    }
    input {
      background: #1f1f1f;
      color: white;
      border: 1px solid #333;
    }
    button {
      background: #e50914;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }
    .note {
      margin-top: 16px;
      font-size: 12px;
      color: #bbb;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="card">
    <h2>StreamHub</h2>
    <form action="/login" method="POST">
      <input type="text" name="username" placeholder="Email or phone number" required>
      <input type="password" name="password" placeholder="Password" required>
      <button type="submit">Sign In</button>
    </form>
    <div class="note">
      Demo only — this is a local mock redirect flow.
    </div>
  </div>
</body>
</html>
"""

HTML_SUCCESS = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome</title>
  <style>
    body {
      margin: 0;
      background: #0b0b0b;
      color: white;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .box {
      background: #161616;
      border: 1px solid #333;
      border-radius: 14px;
      padding: 40px;
      text-align: center;
      width: 520px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.4);
    }
    h1 { color: #e50914; }
    p { color: #ddd; }
    a {
      display: inline-block;
      background: #e50914;
      color: white;
      text-decoration: none;
      padding: 12px 20px;
      border-radius: 8px;
      margin-top: 20px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="box">
    <h1>Welcome to StreamHub</h1>
    <p>This is a mock redirect page used for learning/demo purposes.</p>
    <p>It is running locally and does not connect to any real service.</p>
    <a href="/">Back to Login</a>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_LOGIN

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # fake local validation only
    if username and password:
        return redirect("/success")
    return redirect("/")

@app.route("/success")
def success():
    return HTML_SUCCESS

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
