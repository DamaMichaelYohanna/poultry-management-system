from django.urls import path


from main import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name='home page'),
    path('farm', views.farm_detail, name='farm'),
    path('store', views.StoreView.as_view(), name='store'),
    path('store/add/item', views.add_to_store_item, name='add item'),
    path("store/pickout/<int:pk>", views.pick_out, name='pickout'),

]