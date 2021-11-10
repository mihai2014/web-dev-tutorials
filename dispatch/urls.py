
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('favicon.ico', views.favicon, name = 'favicon'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('topics', views.topics, name = 'topics'),
    path('item/category/<path:href>', views.itemCategory, name = 'category'),
    path('item/<path:file_path>', views.itemTopic, name = 'item'),
    # path('code/<path:file_path>', views.itemTopic, name = 'item'),
    path('test', views.test, name = 'home'),
]
