from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    text = db.Column(db.String(500), nullable=True)

    author = db.Column(db.String(20), default='Anonim')

    def __repr__(self):
        return '<Article %r' % self.id

# =====================================

@app.route('/')
def index():
    articles = Article.query.order_by(Article.id.desc()).all()
    return render_template('index.html', articles=articles)


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/post/<int:id>')
def post(id):
    article = Article.query.get(id)
    return render_template('post.html', article=article)


@app.route('/create-post', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        text_ = request.form['text_']
        author = request.form['author']

        article = Article(title=title, text=text_, author=author)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'Вибачте, трапилась помилка. Спробуйте ще раз.'
    else:
        return render_template('create_post.html')

# =====================================

if __name__ == "__main__":
    app.run(debug=True)