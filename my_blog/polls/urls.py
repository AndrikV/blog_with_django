from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("<int:poll_pk>/", views.handle_detail_view, name='detail'),
    path("<int:poll_pk>/results/", views.handle_results_view, name='results'),
]
