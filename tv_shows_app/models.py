from datetime import date
from django.db import models

class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters."
        if len(postData['desc']) < 10 and len(postData['desc']) >= 1:
            errors['desc'] = "Description must be at least 10 characters."
        if postData['date'] > str(date.today()):
            errors['date'] = "Date must not be in the future."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.CharField(max_length=45)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

