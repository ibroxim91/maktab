from django.db import models

# Create your models here.
class Predmet(models.Model):
	title = models.CharField('Fan nomi',max_length=25)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Classes(models.Model):
	class_number = models.PositiveIntegerField(default=0)
	status = models.BooleanField(default=False)

	def __str__(self):
		return "{} -sinf".format(self.class_number)		


class Question(models.Model):
	predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)
	class_number = models.ForeignKey(Classes, on_delete=models.CASCADE)
	query = models.CharField(max_length=950)
	reg_data = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.query
	
class Variant(models.Model):
	query = models.ForeignKey(Question, on_delete=models.CASCADE)
	variant = models.CharField(max_length=550)
	is_answer = models.BooleanField("To'g'ri javob",default=False)	
	number = models.PositiveIntegerField(default=0, blank=True)
	reg_data = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.variant
	class Meta:
		ordering = ['?']	