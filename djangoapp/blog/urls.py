from django.urls import path
from blog.views import index

# namespace
app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
]
