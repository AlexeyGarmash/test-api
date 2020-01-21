from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('comments/<int:pk>', views.CommentsProductListView.as_view(), name='comment-detail'),
    #path('edit/<int:pk>', views.UserUpdateInfo.as_view()),
] 