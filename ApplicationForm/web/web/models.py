from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class User(AbstractUser):
    ROLES = (
        ('administrator', 'Administrator'),
        ('applicant', 'Applicant'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    class Meta:
        # Add a unique related_name for the groups field
        # to avoid clashes with the default User model
        # reverse accessor
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'
        default_related_name = 'custom_user'

class Course(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    other_details = models.TextField()

class Application(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    entrance_exam_marks = models.DecimalField(max_digits=5, decimal_places=2)
    last_university_attended = models.CharField(max_length=255)
    previous_class_marks = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # Other applicant details fields
    def __str__(self):
        return str(self.user)

