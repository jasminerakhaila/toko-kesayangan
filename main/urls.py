from django.urls import path
from main.views import show_main
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path
# from main import views  # Ganti dengan path yang sesuai jika berbeda
from django.urls import path
from . import views



app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('', views.product_list, name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)