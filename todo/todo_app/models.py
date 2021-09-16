from django.db import models


class Task(models.Model):
    class Unit(models.TextChoices):
        home = 'Home'
        work = 'Work'
        friends = 'Friends'
        hobbies = 'Hobbies'
    unit = models.CharField(max_length=128, choices=Unit.choices, default=Unit.work)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
