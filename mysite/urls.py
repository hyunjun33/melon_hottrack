"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path(route="core/", view=include("core.urls")),
    path(route="hottrack/", view=include("hottrack.urls")),
    path("", RedirectView.as_view(url="/hottrack/")),
    # path("", TemplateView.as_view(template_name="root.html")), #1. 템플릿 응답
    # path("", lambda request: redirect("/core/")), #2. 직접 URL 조합 방식
    # path("", RedirectView.as_view(url="/core/")), #2. 직접 URL 조합 방식
    # path("", lambda request: redirect("core:index")), #3. URL Reverse 활용 방식
    # path("", RedirectView.as_view(pattern_name="core:index")), #3. URL Reverse 활용 방식
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
