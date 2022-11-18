from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import signup, logout_user, login_user, profile, update_profile
from store.views import index, product_detail, add_to_cart, cart, delete_cart
from shop import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('cart/', cart, name='cart'),
    path('cart/delete/', delete_cart, name='delete-cart'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
