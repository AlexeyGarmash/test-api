from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('comments/<int:pk>', views.CommentDeatailView.as_view(), name='comment-detail'),
    #path('edit/<int:pk>', views.UserUpdateInfo.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)