from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5

class User(BaseModel, Base):
	__tablename__ = 'users'
	email = Column(String(128), nullable=False)
	_password = Column(String(128), nullable=False)
	first_name = Column(String(128), nullable=True)
	last_name = Column(String(128), nullable=True)

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, val):
		if val is None or isinstance(val, str) is False:
			self._password = None
		else:
			self._password = str(md5(val.encode()).hexdigest().lower())

	def __str__(self):
		return "[User] {} - {} - {}".format(self.id, self.email, self.display_name())

	def is_valid_password(self, pwd):
		if pwd is None or isinstance(pwd, str) is False or self._password is None:
			return False
		if self._password == str(md5(pwd.encode()).hexdigest().lower()):
			return True
		else:
			return False

	def to_dict(self):
		dct = {}
		for k, v in vars(self).items():
			if k == 'created_at' or k == 'updated_at':
				v = v.strftime("%Y-%m-%d %H:%M:%S")
			if k[0] != '_':
				dct[k] = str(v)
		return dct

	def display_name(self):
		if self.email and self.first_name and self.last_name:
			return "{} {}".format(self.first_name, self.last_name)
		elif self.email and self.first_name is None and self.last_name is None:
			return self.email
		elif self.first_name and self.last_name is None:
			return self.first_name
		elif self.last_name and self.first_name is None:
			return self.last_name
		else:
			return ""