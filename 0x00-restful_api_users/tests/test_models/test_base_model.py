import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

	def test_id(self):
		model = BaseModel()
		model2 = BaseModel()
		self.assertFalse(None, model.id)

	def test_ids_unique(self):
		model = BaseModel()
		model2 = BaseModel()
		self.assertNotEqual(model.id, model2.id)

	def test_created_at(self):
		model = BaseModel()
		self.assertFalse(None, model.created_at)

	def test_updated_at(self):
		model = BaseModel()
		self.assertFalse(None, model.updated_at)
