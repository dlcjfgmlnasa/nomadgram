from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    # 데이터 베이스의 변경이 있기 전
    website = models.URLField(null=True)    # 그래서 이 전에 생성된 유저값에게는 null값을 디폴트로 주라서 설정할 수 있음
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    
    followers = models.ManyToManyField('self')      # 다른 모델이 아니라 User 자신에게 연결을 해야됨
    folloings = models.ManyToManyField('self')


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
