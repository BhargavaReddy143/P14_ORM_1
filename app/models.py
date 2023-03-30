from django.db import models

# Create your models here.
class Topper(models.Model):
    topic_name=models.CharField(max_length=100, primary_key=True)
class Website(models.Model):
    topic_name=models.ForeignKey(Topper, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, unique=True)
    url=models.URLField()
class Players(models.Model):
    name=models.ForeignKey(Website, on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
