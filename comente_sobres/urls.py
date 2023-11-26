from django.urls import path, register_converter
from comente_sobres.models import Topico
from .views import HomePageView, SearchPageView
from .views import like_comment

urlpatterns = [
    path('', SearchPageView.as_view(), name='search'),
    path('home', SearchPageView.as_view(), name='search'),
    path('add_comment', HomePageView.as_view(), name='home_without_param'),
    path('home/<str:nome_topico>/<int:id_topico>', HomePageView.as_view(), name='home_with_param'),
    path('search', SearchPageView.as_view(), name='search'),
    path('like_comment', like_comment, name='like_comment'),
]