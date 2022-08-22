from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/new_comment/", views.create_new_comment, name='new_comment'),
    path("<int:post_pk>/<str:media_name>/", views.get_media, name='get_media'),
    path("<str:media_name>/", views.ShowMedia.as_view(), name='show_media'),
]
