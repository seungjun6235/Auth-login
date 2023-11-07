from django.db import models
from accounts.models import User # 방법1
from django.conf import settings # 방법2
from django.contrib.auth import get_user_model # 방법3

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    #유저모델을 참조하는경우
    # 방법1.(권장X)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    #방법2.(권장0) settings.AUTH_USER_MODEL == 'accounts.User'

    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    #방법3. (권장0)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)