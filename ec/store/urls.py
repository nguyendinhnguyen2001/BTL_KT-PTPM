from django.urls import path
from store.forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from store import views
from ec import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product/', views.show_productView.as_view(), name='product'),
    path('productWomen/', views.show_product_women.as_view(), name='productWomen'),
    path('productMen/', views.show_product_men.as_view(), name='productMen'),
    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),

    path('product_nugioi/', views.product_nugioi, name='product_nugioi'),
    path('product_nugioi/<slug:data>',
         views.product_nugioi, name='product_nugioi_data'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),
         name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',
         form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name="passwordchangedone"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
         form_class=MyPasswordResetForm), name="password_reset"),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
         template_name='app/password_reset_complete.html'), name="password_reset_complete"),

    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
