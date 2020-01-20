from django.urls import include, path
from django.conf.urls import url

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='My API title')),
    path('users/', include('users.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('products/', include('products.urls')),
]
