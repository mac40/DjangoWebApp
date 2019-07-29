from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('create/', login_required(views.CreateArticle.as_view()),
         name='create'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='detail'),
]
