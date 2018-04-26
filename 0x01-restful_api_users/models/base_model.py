from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime, asc, desc
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(object):
	id = Column(String(60), nullable=False, primary_key=True)
	created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
	updated_at = Column(DateTime, nullable=False, default=datetime.utcnow(),
	                    onupdate=datetime.utcnow())

	def __init__(self):
		self.id = uuid4()
		self.created_at = datetime.utcnow()
		self.updated_at = self.created_at

	@classmethod
	def all(cls):
		from models import db_session
		return db_session.query(cls)

	@classmethod
	def count(cls):
		from models import db_session
		return db_session.query(cls).count()

	@classmethod
	def get(cls, id):
		if id is None:
			return None
		from models import db_session
		return db_session.query(cls).get(id)

	@classmethod
	def first(cls):
		from models import db_session
		return db_session.query(cls).order_by(asc(cls.created_at)).first()

	@classmethod
	def last(cls):
		from models import db_session
		return db_session.query(cls).order_by(desc(cls.created_at)).first()
