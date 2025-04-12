from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#NOTES PAGE 
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

    def __str__(self):
        return self.title


#HOMEWORK PAGE 

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)


    def __str__(self):
        return self.title


#TODO_PAGE 
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


#Schedule

class Schedule(models.Model):
    DAY_CHOICES = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]
    name = models.CharField(max_length=255, verbose_name="Task Name")
    time = models.TimeField(verbose_name="Task Time")
    day = models.CharField(max_length=20, choices=DAY_CHOICES, verbose_name="Day of the Week")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Last Updated At")

    def __str__(self):
        return f"{self.name} - {self.day} at {self.time}"
