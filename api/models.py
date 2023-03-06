from django.db import models

class Track(models.Model):
	id = models.IntegerField(primary_key=True)
	activity = models.CharField(max_length=255)
	probability = models.CharField(max_length=255)

	def __str__(self) -> str:
		return self.name
