import sqlite3

import sys

from flask import Flask, jsonify, render_template, request, url_for, redirect, flash
# from werkzeug.exceptions import abort

from loguru import logger


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    # Record a new connection request to the Database
    app.config['DB_CONNECTION_COUNT'] += 1
    return connection


# Function to get a post using its ID
def get_post(post_id):
    my_post = None
    try:
        connection = get_db_connection()
        my_post = connection.execute('SELECT * FROM posts WHERE id = ?',
                                     (post_id, )).fetchone()

    except sqlite3.Error as error:
        logger.error('Error reading from database: \'{}\'', error)

    finally:
        connection.close()

    return my_post


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def fetch_all():
    posts = None
    try:
        connection = get_db_connection()
        posts = connection.execute('SELECT * FROM posts').fetchall()

    except sqlite3.Error as error:
        logger.error('Error reading from database: \'{}\'', error)

    finally:
        connection.close()

    return posts


# Define the main route of the web application
@app.route('/')
def index():
    posts = fetch_all()
    logger.info('Endpoint: /')

    if posts is None:  # Error reading from Database
        return render_template('404.html'), 404

    return render_template('index.html', posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    my_post = get_post(post_id)
    if my_post is None:
        logger.debug('unknown post: [{id}]', id=post_id)
        return render_template('404.html'), 404
    else:
        logger.debug('post: [{id} :: {title}]',
                     id=post_id,
                     title=my_post['title'])
        return render_template('post.html', post=my_post)


# Define the About Us page
@app.route('/about')
def about():
    logger.debug('Endpoint: /about')
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    logger.debug('Endpoint: /create')
    writing_error = False
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            try:
                connection = get_db_connection()
                connection.execute(
                    'INSERT INTO posts (title, content) VALUES (?, ?)',
                    (title, content))
                connection.commit()
            except sqlite3.Error as error:
                writing_error = True
                logger.error('Error writing to database: \'{}\'', error)
            finally:
                connection.close()

            if content is None:
                content_str = ''
            else:
                content_str = str(content)[:80]

            if writing_error:
                logger.error('Error creating post: [{title}]:[{content}]',
                             title=title,
                             content=content_str)
            else:
                logger.debug('post created: [{title}]:[{content}]',
                             title=title,
                             content=content_str)

            return redirect(url_for('index'))

    return render_template('create.html')


@app.route("/healthz")
def get_healthz():
    logger.info('Endpoint: /healtz')
    reading_error = False
    try:
        connection = get_db_connection()
        connection.execute('SELECT * FROM POSTS LIMIT 1').fetchone()

    except sqlite3.Error as error:
        reading_error = True
        logger.error('Error reading from database: \'{}\'', error)

    finally:
        connection.close()

    if reading_error:
        app.config['DB_CONNECTION_COUNT'] = 0  # Reset DB connection count
        message = 'ERROR - unhealthy'
        http_code = 500
    else:
        message = 'OK - healthy'
        http_code = 200

    response = {'status': message}

    return jsonify(response), http_code


@app.route("/metrics")
def get_metrics():
    posts = fetch_all()

    if posts is None:  # Error reading from database
        message = 'ERROR!'
        post_count = 'Unknown'
        app.config['DB_CONNECTION_COUNT'] = 0  # Reset DB connection count
        connection_count = 'Unknown'
    else:
        message = 'OK'
        post_count = len(posts)
        connection_count = app.config['DB_CONNECTION_COUNT']

    response = {"status": message}
    response["data"] = {
        "post_count": post_count,
        "db_connection_count": connection_count
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

    app.config['DB_CONNECTION_COUNT'] = 0
    app.run(host='0.0.0.0', port='3111')
