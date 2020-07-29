from django.db import models

# Create your models here.
class Job(models.Model):
    #Images
    image = models.ImageField(upload_to='images/')
    #Summary
    summary = models.CharField(max_length = 400)
    #Heading
    title = models.CharField(max_length = 100)
    #geturl
    link = models.CharField(max_length = 500)

    def __str__(self):
        return self.title


class Contact(models.Model):
    #email
    email = models.EmailField()
    #Subject
    subject = models.CharField(max_length = 200)
    #message
    message = models.TextField()

    def __str__(self):
        return self.email