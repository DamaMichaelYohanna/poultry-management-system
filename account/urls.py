from django.urls import path


from account import views


app_name = 'account'

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('add', views.add_user, name='add_user'),
    path('update/<int:pk>', views.update_profile, name="update_profile"),
    path('delete/<int:pk>', views.delete_profile, name="delete_profile"),
]