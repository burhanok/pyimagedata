from django.db import models

# Create your models here.

class DeepLearningPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishing_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class MachineLearningPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishing_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class RFLearningPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishing_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DatasciencePost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishing_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
