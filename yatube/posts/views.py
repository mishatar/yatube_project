from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница приложения')


def group_posts(request, slug):
    return HttpResponse('Посты, отфильтрованные по группам')