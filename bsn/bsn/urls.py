from django.contrib import admin
from django.urls import path, include
from users import views as UsersAppViews
from users.views import TestView


user_list = UsersAppViews.TestView.as_view({
    'get': 'example',
})

user_detail = UsersAppViews.TestView.as_view({
    'get': 'example',
})


urlpatterns = [
    #path('users/', include('users.urls')),
    path('users', user_list),
    path('users/<int:pk>', user_detail),
    path('auth', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
