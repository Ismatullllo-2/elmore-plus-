from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for users and posts
users = []
posts = []

@app.route('/')
def index():
    return render_template('index.html', profile_username=None, posts=[])

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
        return render_template('index.html', profile_username=username, posts=posts)
    return redirect(url_for('index'))

@app.route('/post', methods=['POST'])
def post():
    content = request.form['content']
    posts.append(content)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


