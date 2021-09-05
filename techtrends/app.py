import sqlite3

import sys

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

from loguru import logger


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                              (post_id, )).fetchone()
    connection.close()
    return post


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# Define the main route of the web application
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    logger.info('Endpoint: /')

    return render_template('index.html', posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        logger.debug('unknown post: [{id}]', id=post_id)
        return render_template('404.html'), 404
    else:
        logger.debug('post: [{id}]:[{title}]', id=post_id, title=post['title'])
        return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
    logger.debug('Endpoint: /about')
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute(
                'INSERT INTO posts (title, content) VALUES (?, ?)',
                (title, content))
            connection.commit()
            connection.close()

            if content is None:
                content_str = ''
            else:
                content_str = str(content)[:80]

            logger.debug('post created: [{title}]:[{content}]',
                         title=title,
                         content=content_str)

            return redirect(url_for('index'))

    return render_template('create.html')


@app.route("/healthz")
def get_healthz():
    # TODO: Make it dynamic
    response = {'status': 'OK - healthy'}

    logger.info('Endpoint: /healtz')
    return jsonify(response), 200


@app.route("/metrics")
def get_metrics():
    response = {"status": "OK"}
    response["data"] = {
        "post_count": "FILL_THIS",
        "db_connection_count": "FILL_THIS"
    }

    logger.info('Endpoint: /metrics')
    return jsonify(response), 200


# start the application on port 3111
if __name__ == "__main__":
    logger.add(sys.stdout,
               format="{time:YYYY-MM-DD HH:mm:ssZZ} | {level} | {message}",
               level="DEBUG")
    logger.add(sys.stderr,
               format="{time:YYYY-MM-DD HH:mm:ssZZ} | {level} | {message}",
               level="DEBUG")

    app.run(host='0.0.0.0', port='3111')
