from django.conf.urls import url
from . import views

app_name = "images"
urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllImage.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^comments/$',
        view=views.ListAllComments.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^likes/$',
        view=views.ListAllLike.as_view(),
        name='all_images'
    ),
]