from django.urls import path

from jangoPro1 import settings
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('profile/',views.profile,name='user_profile'),
    path('create/', views.create_view, name='create_view'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('boot/', views.boot, name='boot'),
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('reset_pass', views.pass_reset, name="password_reset"),
    path('forget_pass/', views.forget_pass, name="forget_password"),
    # path('reset_password/<uidb64>/<token>', views.save_pass, name="password_reset_confirm")

    # path('reset_password/', auth_view.PasswordResetView.as_view(template_name='password_reset_view.html'),
    #      name='password_reset'),
    # path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    #      name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
