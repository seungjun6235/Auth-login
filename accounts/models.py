from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    # aritcle_set = 자동 컬럼추가
    # comment_set 