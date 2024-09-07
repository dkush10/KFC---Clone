from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('menu',menu,name='menu'),
    path('cart',cart,name='cart'),
    path('addtocart|<int:id>',addtocart,name='addtocart'),
    path('remove|<int:id>',remove,name='remove'),
    path('removeall',removeall,name='removeall'),
    path('checkout',checkout,name='checkout'),
    path('contactus',contactus,name='contactus'),
    path('profile',profile,name='profile'),
    path('updateprofile|<int:id>',updateprofile,name='updateprofile'),
    path('changepassword|<int:id>',changepassword,name='changepassword'),
    path('logout',logout_,name='logout'),
    path('deleteprofile|<int:id>',deleteprofile,name='deleteprofile'),
    path('aboutus',aboutus,name='aboutus'),
    path('quantityplus|<int:id>',quantityplus,name='quantityplus'),
    path('quantityminus|<int:id>',quantityminus,name='quantityminus'),
    path('aboutus',aboutus,name='aboutus'),
    path('orderplaced',orderplaced,name='orderplaced'),
]