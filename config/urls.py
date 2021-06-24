"""freecodeschool URL Configuration
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/certificates/', include('apps.certificates.urls')),
    path('api/v1/lectures/', include('apps.lectures.urls'))
]

