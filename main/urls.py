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
#     urls for products
    path('product/dashboard', views.product_dashboard, name='product dashboard'),
    path('product/add', views.product_add, name='product add'),
    path('product/update', views.product_update, name='product update'),
    path('product/delete/<int:pk>', views.product_delete, name='product delete'),

]