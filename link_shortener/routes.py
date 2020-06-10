from flask import Blueprint, render_template, request, redirect
from .extensions import db
from .models import  Link

short = Blueprint("short", __name__)

@short.route('/<short_url>')
def url_redirect(short_url):
	link = Link.query.filter_by(short_url=short_url).first_or_404()
	return redirect(link.original_url)

@short.route('/')
def index():
	return render_template('index.html')

@short.route('/send_link', methods=['POST'])
def send_link():
	original_url = request.form['original_url']
	link = Link(original_url=original_url)
	db.session.add(link)
	db.session.commit()

	return render_template('short_link.html', new = link.short_url, original_url = link.original_url)

@short.errorhandler(404)
def error_page(error):
	return render_template('404.html')