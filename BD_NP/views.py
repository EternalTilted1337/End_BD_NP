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
    paginate_by = 10 # вот так мы можем указать количество записей на странице

def get_queryset(self):
   # Получаем обычный запрос
   queryset = super().get_queryset()
   # Используем наш класс фильтрации.
   # self.request.GET содержит объект QueryDict, который мы рассматривали
   # в этом юните ранее.
   # Сохраняем нашу фильтрацию в объекте класса,
   # чтобы потом добавить в контекст и использовать в шаблоне.
   self.filterset = Post(self.request.GET, queryset)
   # Возвращаем из функции отфильтрованный список товаров
   return self.filterset.qs


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Добавляем в контекст объект фильтрации.
    context['filterset'] = self.filterset
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



