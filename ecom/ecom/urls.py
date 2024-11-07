from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('products.urls')),
    path('customer/',include('customers.urls')),
    path('order/',include('orders.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #new
