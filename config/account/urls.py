from django.contrib.auth import views
from django.urls import path, include
from .views import PasswordChange,Register,activate,user_selected_courses,home
from django.contrib.auth import views as auth_views



app_name='account'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('register/',Register.as_view(),name='register'),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path(
        "password_change/", PasswordChange.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view
        (),
        name="password_reset_done",
    ),

    path('', include('django.contrib.auth.urls')),


    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

]


urlpatterns+=[
    path('',home,name='home'),
    path('user_selected_courses/', user_selected_courses, name='user_selected_courses'),

]