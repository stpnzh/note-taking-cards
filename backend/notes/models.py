from django.db import models
from django.utils.timezone import now



class Tag(models.Model):
  text = models.CharField(max_length=200)

  def __str__(self):
    return self.text


class Note(models.Model):
  cat = models.CharField(max_length=200)
  desc = models.TextField()
  content = models.TextField()
  pub_date = models.DateTimeField('date published', default=now)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

  def __str__(self):
    return self.desc
  


  
