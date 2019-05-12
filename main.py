from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://building-a-blog:building@localhost:8889/building-a-blog'
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
        title = ""
        body = ""

        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            new_post = Blog(title, body)
            db.session.add(new_post)
            db.session.commit()
            
            #return redirect('/blog?id={}'.format(new_post.id))
        return render_template('new_blog.html')

    @app.route('/blog', methods=['GET'])
    def  blog_list():
        b_list = Blog.query.all()
        post_page_id = request.args.get('id')

        if post_page_id == None:
            return render_template('blog_list.html', title='My Blog List', b_list=b_list)
        else:
            blog = Blog.query.get(post_page_id)
            return render_template('new_blog.html', blog=blog)
        
          
        
        return render_template('blog_list.html', title='My Blog List', b_list=b_list)

if __name__ == '__main__':
    app.run()