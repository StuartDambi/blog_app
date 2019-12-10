from flask import Flask, render_template

app = Flask(__name__)
# noinspection PyInterpreter
blog = {
    'name': 'My first Flask App',
    'posts': {}
}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/post/<int:post_id>')
def posts(post_id):
    post = blog['posts'].get(post_id)
    if post is not None:
        return render_template('posts.jinja2', template_post=post)
    else:
        return render_template('404.html', message=f'Post with id {post_id} does not Exist')


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body ')
    return render_template('create.html')


app.run()
