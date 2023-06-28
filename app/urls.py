from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm, mypasswordchangform, MypasswordrestForm, MysetForm
from django.contrib.auth import views as auth_view
urlpatterns = [
    # all product showing in home 
    path('', views.productview.as_view(), name='home'),

    # perticular one product in showing in product page
    path('product-detail/<int:pk>', views.productdetailview.as_view(), name='product-detail',),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', views.show_cart, name='showcart'),
    
    path('buy/', views.buy_now, name='buy-now'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('address/', views.AddressView.as_view(), name='address'),
    
    path('orders/', views.orders, name='orders'),
    
    # change password using auth
    path('change-password/', auth_view.PasswordChangeView.as_view(template_name="app/change_password.html", form_class=mypasswordchangform, success_url='/passwordchangedone/'), name='changepassword'),

    # after change password redirect to success page 
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),


    # password reset process
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MypasswordrestForm), name='password_reset'), 
    
    
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'), 

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MysetForm), name='password_reset_confirm'), 

    path('password-reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'), 

    
    
    
    # use all mobile showing to mobile page 
    path('mobile/', views.mobile, name='mobile'),
    
    # use filter catgory mobile show in mobile page
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    path('topwear/', views.topwear, name='topwear'),
    
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),
    
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form = LoginForm, next_page='home') ,name='login'),

    path('logout/',auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('register/', views.Customerregisternation.as_view(), name='register'),
    
    path('checkout/', views.checkout, name='checkout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
