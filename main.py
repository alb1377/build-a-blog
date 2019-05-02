from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:building@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blog', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name = request.form['blog']
        new_blog = Blog(blog_name)
        db.session.add(new_blog)
        db.session.commit()
    
    return render_template('form.html', title="Blog")







@app.route('/newpost', methods =)






if __name__ == '__main__':
    app.run()