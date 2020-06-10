from .extensions import db
from datetime import datetime
import random

class Link(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	original_url = db.Column(db.String(1000))
	short_url = db.Column(db.String(7), unique = True)
	create_date = db.Column(db.DateTime, default=datetime.now)

	def __init__(self,**kwargs):
		super().__init__(**kwargs)

		check_org_url = self.query.filter_by(original_url=self.original_url).first()

		#if the url passed has already been shortened just return 
		#that one instead of generating a new one
		if self.original_url != check_org_url:
			self.short_url = self.short_link_gen()

		else:
			self.short_url = check_org_url.short_url

	def short_link_gen(self):
		no = random.randrange(0,10000000000)
		short_url = ''.join(str(no))

		link = self.query.filter_by(short_url=short_url).first()

		#if generated link already exists make new one
		if link:
			return self.short_link_gen()

		else:
			return short_url