from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCGEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:building@localhost:8889/building-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column (db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body
    
    @app.route('/newpost', methods=['POST', 'GET'])

    def start_post():
        if request.method == 'POST':
            new_blog = request.form['blog_post']
            new_post = Blog(new_blog)
            db.session.add(new_post)
            db.session.commit()
        
        return render_template(new_blog.html, title="Blog It Up",blog_post=blog_post)

    @app.route('/blog', methods=['POST', 'GET'])
    def  blog_list():
        if request.method == 'POST':
            blog_list = request.form['list']
            postings = Blog(blog_list)
            db.session.add(postings)
            db.session.commit()
        
        return render_template(blog_list.html, title="My Blog List")

if __name__ == '__main__':
    app.run()