from django.db import models

class contact:

	def __init__(self, id, contactNumbers, name):
		self.id = id
		self.contactNumbers = contactNumbers
		self.name = name
