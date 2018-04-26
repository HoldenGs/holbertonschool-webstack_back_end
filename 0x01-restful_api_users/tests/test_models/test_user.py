import unittest
from models.user import User

class TestUser(unittest.TestCase):

	# user.to_dict()

	def test_to_dict_no_pwd(self):
		user = User()
		user.password = "Hello World"
		d = user.to_dict()
		self.assertEqual(None, d.get('password'))

	def test_to_dict_time_strings(self):
		user = User()
		d = user.to_dict()
		self.assertIsInstance(d['created_at'], str)
		self.assertIsInstance(d['updated_at'], str)

	def test_to_dict_attributes(self):
		user = User()
		user.first_name = "John"
		user.last_name = "Nash"
		user.email = "supernash@gmail.com"
		d = user.to_dict()
		self.assertEqual(d['first_name'], "John")
		self.assertEqual(d['last_name'], "Nash")
		self.assertEqual(d['email'], "supernash@gmail.com")

	# user.is_valid_password()

	def test_is_valid_password_pwd_none(self):
		user = User()
		user.password = "Hello World"
		self.assertFalse(user.is_valid_password(None))

	def test_is_valid_password_nonstr(self):
		user = User()
		user.password = 111
		self.assertFalse(user.is_valid_password(111))

	def test_is_valid_password_none(self):
		user = User()
		user.password = None
		self.assertFalse(user.is_valid_password("Hello World"))

	def test_is_valid_password_wrong(self):
		user = User()
		user.password = "Hello World"
		self.assertFalse(user.is_valid_password("Hulu World"))

	def test_is_valid_password_correct(self):
		user = User()
		user.password = "Hello World"
		self.assertTrue(user.is_valid_password("Hello World"))

	# user.password getter and setter

	def test_password_get(self):
		user = User()
		self.assertEqual(None, user.password)

	def test_password_set_obfuscated(self):
		user = User()
		user.password = "Hello World"
		self.assertNotEqual("Hello World", user.password)

	def test_password_set_lowercase(self):
		user = User()
		user.password = "Hello World"
		self.assertTrue(user.password.islower())

	def test_password_set_none(self):
		user = User()
		user.password = 111
		self.assertEqual(None, user.password)

	# user.display_name()

	def test_display_name_full(self):
		user = User()
		user.first_name = "John"
		user.last_name = "Nash"
		user.email = "supernash@gmail.com"
		self.assertEqual("John Nash", user.display_name())

	def test_display_name_first(self):
		user = User()
		user.first_name = "John"
		self.assertEqual("John", user.display_name())

	def test_display_name_last(self):
		user = User()
		user.last_name = "Nash"
		self.assertEqual("Nash", user.display_name())

	def test_display_name_email(self):
		user = User()
		user.email = "supernash@gmail.com"
		self.assertEqual("supernash@gmail.com", user.display_name())

	def test_display_name_none(self):
		user = User()
		self.assertEqual("", user.display_name())

	# user.__str__()

	def test_user_str_full(self):
		user = User()
		user.email = "supernash@gmail.com"
		user.first_name = "John"
		user.first_name = "Nash"
		eq_str = "[User] {} - {} - {}".format(user.id,
		                                      user.email,
		                                      user.display_name())
		self.assertEqual(eq_str, user.__str__())

	def test_user_str_email(self):
		user = User()
		user.email = "supernash@gmail.com"
		eq_str = "[User] {} - {} - {}".format(user.id, user.email, user.email)
		self.assertEqual(eq_str, user.__str__())

	def test_user_str_none(self):
		user = User()
		self.assertEqual("[User] {} - None - ".format(user.id), user.__str__())