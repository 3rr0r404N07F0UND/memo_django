from django.db import models

# Create your models here.

class User(models.Model):
  user_id = models.CharField(max_length = 20, unique = True, null = False)
  user_pw = models.CharField(max_length = 64, null = False)

class Memo(models.Model):
  memo_title = models.CharField(max_length = 255, unique = True, null = False)
  memo_text = models.TextField()
  memo_id = models.CharField(max_length = 20, null = False, default = "sia")
  memo_time = models.DateTimeField(auto_now = True)
