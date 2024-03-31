from flask import Blueprint, render_template
from app.articles.models import Article
blueprint = Blueprint('post', __name__)


@blueprint.route('/article/<int:article_id>')
def detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('front/detail.html', article=article)
