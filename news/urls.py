from django.urls import path
from news.views import news_list_view, news_detail_view


urlpatterns = [
    path('', news_list_view, name='news_list_url'),
    path('<int:id>/', news_detail_view, name='news_detail_url'),
]