from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductHome.as_view() , name = 'home'),
    path('about/', about, name = 'about'),
    path('promotion/', promotion, name = 'promotion'),
    path('cart/', cart, name = 'cart'),
    path('login/', login, name = 'login'),
    path('post/<slug:post_slug>/', show_post, name = 'post'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name = 'category'),
    
    
    # path('models/<int:model_id>/', models),
    

]