from django.urls import path
from . import views


urlpatterns = [

    path('launch/', views.laucning),


    path('login/', views.loginpage),
    path('login_post/', views.login_post),
    path('shophome/', views.homepage),

    path('product/', views.add_product),
    path('product_post/', views.product_post),
    path('view_product/', views.view_product),
    path('delete_product/<str:id>', views.delete_product),
    path('edit_product/<str:id>', views.edit_product),
    path('edit_post/', views.edit_post),

    path('view_users/', views.view_users),
    path('view_orders/', views.view_orders),
    path('viewmore/<str:id>', views.viewmore),
    path('update_status/<str:id>', views.update_status),

    path('signup/', views.signup),
    path('signup_post/', views.signup_post),
    path('userhome/', views.userhome),

    path('userviewproduct/', views.userviewproduct),

    path('addcart/<str:id>', views.addtocart),
    path('cartpost/', views.cartpost),
    path('viewcart/', views.viewcart),
    path('deletcart/<str:id>', views.deletcart),

    path('saveadrs/', views.saveadrs),
    path('savedrs_post/', views.savedrs_post),
    path('viewmyadrs/', views.viewmyadrs),
    path('delete_adrs/<str:id>', views.delete_adrs),
    path('editadrs/<str:id>', views.editadrs),
    path('edit_adrsPost/', views.edit_adrsPost),


    path('payment/', views.payment_page, name='payment_page'),
    path('process_payment/', views.process_payment, name='process_payment'),

    path('myorder/', views.view_myorder),
    path('my_ordermore/<str:id>', views.my_ordermore),

    path('rating/<str:id>', views.rating_page),
    path('send_rating/', views.send_rating),


    path('logout/', views.logout_view, name='logout'),
]