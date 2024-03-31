from flask import Blueprint, render_template, request
from app.articles.models import Article

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def home():
    articles = Article.query.all()
    page = request.args.get('page', 1, type=int)
    per_page = 1
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(articles) + per_page)
    items_on_page = articles[start:end]
    return render_template('front/home.html', articles=items_on_page, total_pages=total_pages, page=page)
