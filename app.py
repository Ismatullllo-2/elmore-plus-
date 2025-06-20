from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for users and posts
users = []
posts = []

# HTML template with embedded CSS
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Network</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        input {
            padding: 10px;
            margin: 5px 0;
            width: 100%;
            max-width: 300px;
        }
        button {
            padding: 10px;
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
        .profile {
            margin-top: 20px;
            padding: 15px;
            background-color: white;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>

    <h1>Welcome to the Social Network!</h1>

    <h2>Registration</h2>
    <form action="/register" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>

    <h2>Login</h2>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>

    {% if profile_username %}
    <div class="profile">
        <h2>Profile: {{ profile_username }}</h2>
        <h3>Posts:</h3>
        <div id="posts">
            {% for post in posts %}
                <div>{{ post }}</div>
            {% endfor %}
        </div>
        <form action="/post" method="post">
            <textarea name="content" placeholder="What's new?" rows="3" required></textarea>
            <button type="submit">Post</button>
        </form>
    </div>
    {% endif %}

</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template, profile_username=None, posts=[])

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    users.append({'username': username, 'password': password})
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if user:
        return render_template_string(html_template, profile_username=username, posts=posts)
    return redirect(url_for('index'))

@app.route('/post', methods=['POST'])
def post():
    content = request.form['content']
    posts.append(content)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

