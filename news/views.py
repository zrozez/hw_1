from django.shortcuts import render, get_object_or_404

from news.models import News
from news.forms import NewsForm


def news_list_view(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', context={'news': news})


def news_detail_view(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', context={'news': news})


