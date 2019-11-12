from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('user/', views.UserListView.as_view(), name='users'),
    path('user/<int:pk>/', views.UserInfoDetailView.as_view(), name='userinfo-detail'),
    path('timeline/', views.index, name='timeline'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('add_picture/', views.index, name='add_picture'),
    path('notification/', views.index, name='notification'),
    path('profile/', views.index, name='profile'),
    path('edit_profile/', views.index, name='edit_profile'),
    path('settings/', views.index, name='settings'),
    path('', views.index, name='index'),
    #url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.profile),
    #url(r'^logout/$', views.logoutView, name='logout'),
]