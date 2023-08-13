from django.views.generic import ListView
from BD_NP.models import Post
from django.views.generic.detail import DetailView
from django.shortcuts import render
from datetime import datetime

class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'object'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.object_list.first().id
        return context

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
    pk_url_kwarg = 'id'


def news_list(request):
    articles = Post.objects.order_by('-date')
    total_news_count = articles.count()
    return render(request, 'news_list.html', {'articles': articles, 'total_news_count': total_news_count})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context

from django.shortcuts import render

