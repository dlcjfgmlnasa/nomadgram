from django.contrib import admin
from . import models


# Register your models here.
# 여기는 admin 페이지를 어떻게 보이는지를 만들어주는 역할
# 데코레이터를 달아줘야됨

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
