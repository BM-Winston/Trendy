from django.conf import settings
from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name = 'home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('businesses/', views.businesses, name='businesses'),
    path('n_hood/', views.n_hood, name='n_hood'),
    path('create_business/', views.create_business, name='create_business'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
