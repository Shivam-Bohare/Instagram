from django.urls import path
from . import views
#from .views import EditUserInfoView
from django.conf.urls import url, include
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    
    # url(r'^profiles/new/$', NewUserInfoView.as_view(), name="new-user-profile"),
    # url(r'^users/(?P<pk>\d+)/edit/$', EditUserInfoView.as_view(), name="edit-user-profile"),
    
    path('user/', views.UserListView.as_view(), name='users'),
    path('user/<int:pk>/', views.userInfoDetailView, name='userinfo-detail'),
    path('timeline/', views.index, name='timeline'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('add_picture/', views.picture_view, name='add_picture'),
    path('notification/', views.index, name='notification'),
    path('profile/', views.index, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.index, name='settings'),
    path('', views.index, name='index'),
    #url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.profile),
    #url(r'^logout/$', views.logoutView, name='logout'),
    

]