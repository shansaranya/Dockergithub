from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Basic HTML template with a login placeholder
LOGIN_HTML = """
<!doctype html>
<title>Simple Login Page</title>
<h1>Welcome!</h1>
<p>This is a containerized Python web app.</p>
<h2>Login</h2>
<form method="POST" action="/login">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username" value="user"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password" value="pass"><br><br>
    <input type="submit" value="Log In">
</form>
<p>Note: This is a placeholder; it always redirects to Home.</p>
"""

@app.route('/')
def home():
    """Renders the simple login placeholder page."""
    return render_template_string(LOGIN_HTML)

@app.route('/login', methods=['POST'])
def login():
    """Placeholder for login logic - always redirects to home for this example."""
    # In a real app, you would validate credentials here
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Attempted login with: {username}/{password}")
    return redirect(url_for('home')) # Redirect back to the home page

if __name__ == '__main__':
    # Run on all public IPs on port 5000, as is common for Docker
    app.run(host='0.0.0.0', port=5000)
