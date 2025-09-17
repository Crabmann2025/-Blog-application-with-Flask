from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Pfad zur JSON-Datei
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_FILE = os.path.join(BASE_DIR, "posts.json")


# Blog-Beiträge laden
def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r") as file:
            return json.load(file)
    return []


# Blog-Beiträge speichern
def save_posts(posts):
    with open(POSTS_FILE, "w") as file:
        json.dump(posts, file, indent=4)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


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
            "content": content
        }

        blog_posts.append(new_post)
        save_posts(blog_posts)

        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
