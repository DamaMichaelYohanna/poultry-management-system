from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name='home page'),
    path('farm', views.farm_detail, name='farm'),
    path('store', views.StoreView.as_view(), name='store'),
    path('store/item/add', views.add_to_store_item, name='add item'),
    path('store/item/restock', views.restock, name='restock'),
    path("store/item/pickout/<int:pk>", views.pick_out, name='pickout'),
    #     urls for for sales products
    path('product/dashboard', views.product_dashboard,
         name='product_dashboard'),
    path('product/update/<int:pk>', views.product_update, name='product update'),
    path('product/delete/<int:pk>', views.product_delete,
         name='product delete'),
    path('product/add_to_cart/<int:pk>', views.add_to_cart, name='add to cart'),
    path('product/remove_from_cart/<int:pk>', views.remove_from_cart,
         name='remove from cart'),
    path("product/clear_cart", views.clear_cart, name="clear cart"),
    path('product/checkout', views.checkout, name='checkout'),
    #     url for invoice
    path("invoice/<str:ref>", views.single_invoice, name='invoice'),
    path("invoices", views.all_invoice, name='all_invoice'),
    #     urls for storage products
    path('product/management/category', views.category_management,
         name='category_management'),
    path('product/management/product', views.product_management,
         name='product_management'),
]
