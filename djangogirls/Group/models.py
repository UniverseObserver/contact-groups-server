from django.db import models

class group:

	def __init__(self, id, listOfContacts, nameOfGroup):
		self.id = id
		self.listOfContacts = listOfContacts
		self.nameOfGroup = nameOfGroup
