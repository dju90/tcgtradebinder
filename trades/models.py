import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

# class User(models.Model):
# 	name = models.CharField(max_length=200)
# 	join_date = models.DateTimeField('date joined')
# 	zip = models.CharField(max_length=20)
#
# 	def __str__(self):
# 		return self.name
#
# 	def joined_recently(self):
# 		return self.join_date >= timezone.now() - datetime.timedelta(days=1)

class Binder(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type

class Card(models.Model):
	binder = models.ForeignKey(Binder, on_delete=models.CASCADE)
#
# 	# a unique id for this card in Scryfall's database
# 	scryfall_id = models.IntegerField()
#
# 	# A unique ID for this card’s oracle identity.
# 	# This value is consistent across reprinted card editions,
# 	# and unique among different cards with the same name (tokens, Unstable variants, etc).
# 	oracle_id = models.IntegerField()
#
	name = models.CharField('card name', max_length=200)
	expansion = models.CharField('expansion', max_length=3)
	condition = models.CharField('condition', max_length=2)
	foil = models.BooleanField('foil', default=False)
# 	quantity = models.IntegerField('quantity', default=1)
#
# 	# price to be provided by tcgplayer api
# 	price = models.FloatField('price', default=0)


