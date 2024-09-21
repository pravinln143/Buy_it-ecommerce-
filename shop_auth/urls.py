from django.urls import path
from shop_auth import views
from shop_auth.views import signup, ActivateAccountView, handlelogin, handlelogout
from django.urls import path
from .views import handlelogin, handlelogout, signup, ActivateAccountView

urlpatterns = [
    path('login/', handlelogin, name='login'),         # URL pattern for login
    path('logout/', handlelogout, name='logout'),      # URL pattern for logout
    path('signup/', signup, name='signup'),            # URL pattern for signup
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    

]

