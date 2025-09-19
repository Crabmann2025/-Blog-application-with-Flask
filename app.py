from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_FILE = os.path.join(BASE_DIR, "posts.json")



# Helper Functions

def load_posts():
    """
    Load all blog posts from the JSON file.

    Returns:
        list: A list of blog post dictionaries. Returns an empty list if file does not exist or JSON is invalid.
    """
    try:
        if os.path.exists(POSTS_FILE):
            with open(POSTS_FILE, "r") as file:
                return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading posts: {e}")
    return []


def save_posts(posts):
    """
    Save the list of posts to the JSON file.

    Args:
        posts (list): List of blog post dictionaries.
    """
    try:
        with open(POSTS_FILE, "w") as file:
            json.dump(posts, file, indent=4)
    except IOError as e:
        print(f"Error saving posts: {e}")


def fetch_post_by_id(posts, post_id):
    """
    Fetch a single post by its ID.

    Args:
        posts (list): List of post dictionaries.
        post_id (int): ID of the post to fetch.

    Returns:
        dict or None: The post dictionary if found, else None.
    """
    for post in posts:
        if post["id"] == post_id:
            return post
    return None



# Routes

@app.route('/')
def index():
    """Render the homepage with all blog posts."""
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add a new blog post."""
    blog_posts = load_posts()
    if request.method == 'POST':
        author = request.form.get("author").strip()
        title = request.form.get("title").strip()
        content = request.form.get("content").strip()

        # Basic input validation
        if not author or not title or not content:
            flash("All fields are required!", "danger")
            return redirect(url_for('add'))

        new_id = max([post["id"] for post in blog_posts], default=0) + 1
        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
            "likes": 0
        }

        blog_posts.append(new_post)
        save_posts(blog_posts)
        flash("Post added successfully!", "success")
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Update an existing blog post."""
    blog_posts = load_posts()
    post = fetch_post_by_id(blog_posts, post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get("author").strip()
        title = request.form.get("title").strip()
        content = request.form.get("content").strip()

        if not author or not title or not content:
            flash("All fields are required!", "danger")
            return redirect(url_for('update', post_id=post_id))

        post['author'] = author
        post['title'] = title
        post['content'] = content
        save_posts(blog_posts)
        flash("Post updated successfully!", "success")
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Delete a blog post (POST request for safety)."""
    blog_posts = load_posts()
    post = fetch_post_by_id(blog_posts, post_id)
    if not post:
        flash("Post not found!", "danger")
        return redirect(url_for('index'))

    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    save_posts(blog_posts)
    flash("Post deleted successfully!", "success")
    return redirect(url_for('index'))


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    """Increment the like counter of a post."""
    blog_posts = load_posts()
    post = fetch_post_by_id(blog_posts, post_id)
    if post:
        post["likes"] = post.get("likes", 0) + 1
        save_posts(blog_posts)
        flash("You liked this post!", "success")
    else:
        flash("Post not found!", "danger")
    return redirect(url_for('index'))



# Run the App

if __name__ == '__main__':
    app.run(debug=True)
