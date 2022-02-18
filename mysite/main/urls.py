from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('categories/<int:category_id>/', views.category, name='category'),
    path('products/<int:product_id>', views.product, name='product'),
]

if settings .DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
