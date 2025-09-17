from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_FILE = os.path.join(BASE_DIR, "posts.json")

# Load blog posts
def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save blog posts
def save_posts(posts):
    with open(POSTS_FILE, "w") as file:
        json.dump(posts, file, indent=4)

# Helper: fetch a single post by ID
def fetch_post_by_id(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            return post
    return None

# Index route
@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

# Add new post
@app.route('/add', methods=['GET', 'POST'])
def add():
    blog_posts = load_posts()
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        new_id = max([post["id"] for post in blog_posts], default=0) + 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
            "likes": 0  # Neues Feld für Likes
        }

        blog_posts.append(new_post)
        save_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('add.html')

# Delete a post
@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_posts = load_posts()
    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    save_posts(blog_posts)
    return redirect(url_for('index'))

# Update a post
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    blog_posts = load_posts()
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['author'] = request.form.get("author")
        post['title'] = request.form.get("title")
        post['content'] = request.form.get("content")
        save_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)

# Like a post
@app.route('/like/<int:post_id>')
def like(post_id):
    blog_posts = load_posts()
    # Direkt die Liste durchgehen und das passende Post-Dictionary ändern
    for post in blog_posts:
        if post["id"] == post_id:
            post["likes"] = post.get("likes", 0) + 1
            break
    save_posts(blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
