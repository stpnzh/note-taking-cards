from django.db import models
from django.utils.timezone import now


class Note(models.Model):
  category = models.CharField(max_length=200)
  description = models.TextField()
  code = models.TextField()
  pub_date = models.DateTimeField('date published', default=now)

  def __str__(self):
    return self.description
  

class Tag(models.Model):
  note = models.ForeignKey(Note, on_delete=models.CASCADE)
  tag = models.CharField(max_length=200)

  def __str__(self):
    return self.tag
  
