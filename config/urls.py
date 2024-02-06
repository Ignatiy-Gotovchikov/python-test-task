from django.contrib import admin

from django.urls import path, include

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('', include('newsfeed.urls')),

    path('accounts/', include('allauth.urls')),
]

