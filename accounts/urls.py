from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),  
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
    path('profile/', views.accountSettings, name="profile"),
	path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.delete),


	# path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	# path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	# path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	# path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
# 	path('lupa/', views.lupa, name="lupa"),
# 	path('lupaada/', views.lupaada, name="lupaada"),
# 	path('lupatidak/', views.lupatidak, name="lupatidak"),
# 	path('GantiPassword/', views.GantiPassword, name="GantiPassword"),
# 	path('password-reset/',auth_views.PasswordResetView.as_view(
#              template_name='users/password_reset.html'),name='password_reset'),
#     path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
#              template_name='users/password_reset_done.html'), name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
#              template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
#     path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
#              template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ]