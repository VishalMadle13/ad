

# Create your models here.




from django.db import models
from django.conf import settings

# Create your models here.
class Faculty(models.Model):

	name=models.CharField(max_length=255,default='')
	# id=models.CharField(max_length=255,default='')
	# course_id=models.CharField(max_length=255,default='')
	# sec_id=models.CharField(max_length=255,default='')
	# semester=models.CharField(max_length=255,default='')
	# year=models.CharField(max_length=255,default='')
	password=models.CharField(max_length=255,default='')
	email=models.CharField(max_length=255,default='')
	username=models.CharField(max_length=255,default='')

	def __str__(self):
		return f'{self.name}'




class Student(models.Model):

	name=models.CharField(max_length=255,default='')
	email=models.CharField(max_length=255,default='')
	username=models.CharField(max_length=255,default='')
	password=models.CharField(max_length=255,default='')
	rollNo=models.CharField(max_length=50,default='')


	def __str__(self):
		return f'{self.name} {self.rollNo}'


class Classroom(models.Model):

	building=models.CharField(max_length=255,default='')
	room_number=models.CharField(max_length=255,default='')
	capacity=models.IntegerField()


	def __str__(self):
		return f'{self.building} {self.room_number}'

class Department(models.Model):

	dept_name=models.CharField(max_length=255,default='')
	room_number=models.CharField(max_length=255,default='')
	capacity=models.IntegerField()

	def __str__(self):
		return f'{self.dept_name} {self.room_number}'


class Course(models.Model):

	course_id=models.CharField(max_length=255,default='')
	title=models.CharField(max_length=255,default='')
	dept_name=models.CharField(max_length=255,default='')
	credits=models.IntegerField()


	def __str__(self):
		return f'{self.title} {self.course_id}'

class Instructor(models.Model):

	ins_id=models.CharField(max_length=255,default='')
	name=models.CharField(max_length=255,default='')
	dept_name=models.CharField(max_length=255,default='')
	salary=models.CharField(max_length=255,default='')

	def __str__(self):
		return f'{self.name} {self.rollNo}'

class Section(models.Model):

	course_id=models.CharField(max_length=255,default='')
	sec_id=models.CharField(max_length=255,default='')
	semester=models.CharField(max_length=255,default='')
	year=models.CharField(max_length=255,default='')
	building=models.CharField(max_length=255,default='')
	room_number=models.CharField(max_length=255,default='')
	time_slot_id=models.CharField(max_length=255,default='')
	

	def __str__(self):
		return f'{self.course_id} {self.sec_id}'

class Takes(models.Model):

	takes_id=models.CharField(max_length=255,default='')
	course_id=models.CharField(max_length=255,default='')
	sec_id=models.CharField(max_length=255,default='')
	semester=models.CharField(max_length=255,default='')
	year=models.CharField(max_length=255,default='')
	grade=models.CharField(max_length=255,default='')

	def __str__(self):
		return f'{self.id} {self.course_id}'

class Advisor(models.Model):

	s_id=models.CharField(max_length=255,default='')
	i_id=models.CharField(max_length=255,default='')

	def __str__(self):
		return f'{self.s_id} {self.i_id}'

class Time_slot(models.Model):

	time_slot_id=models.CharField(max_length=255,default='')
	day=models.CharField(max_length=255,default='')
	start_time=models.CharField(max_length=255,default='')
	year=models.CharField(max_length=255,default='')
	grade=models.CharField(max_length=255,default='')
	

	def __str__(self):
		return f'{self.time_slot_id} {self.day}'

class Prereq(models.Model):

	course_id=models.CharField(max_length=255,default='')
	prereq_id=models.CharField(max_length=255,default='')

	def __str__(self):
		return f'{self.course_id} {self.prereq_id}'
	

