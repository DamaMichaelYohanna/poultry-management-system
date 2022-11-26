from django.urls import path


from main import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name='home page'),
    path('farm', views.farm_detail, name='farm'),
    path('store', views.Store.as_view(), name='store'),
    path("store/pickout", views.pick_out, name='pickout'),

]