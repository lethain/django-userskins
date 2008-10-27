from django.db import models
from django.contrib.auth.models import User

class SkinPreference(models.Model):
    user = models.ForeignKey(User)
    skin = models.CharField(max_length=20)from django.db import models
