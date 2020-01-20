from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('detail/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('edit/<int:pk>', views.UserUpdateInfo.as_view()),
]
