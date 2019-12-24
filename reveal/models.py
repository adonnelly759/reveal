from django.db import models

# Create your models here.
class Codes(models.Model):
    code = models.CharField(max_length=255)
    sub = models.IntegerField(default=0)

class Question(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.CharField(max_length=255)
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.q.title, self.title)