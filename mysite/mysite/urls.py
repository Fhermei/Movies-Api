"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MoviedataViewSet, ActiondataViewSet, AdventuredataViewSet, ComedydataViewSet
from movies.views import ChildrendataViewSet, CrimedataViewSet, RomancedataViewSet, DramadataViewSet
from movies.views import AnimationdataViewSet, HistorydataViewSet, MysterydataViewSet, WardataViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('movies', MoviedataViewSet, basename='movies')
router.register('action', ActiondataViewSet,'Action')
router.register('adventure', AdventuredataViewSet,'adventure')
router.register('comedy', ComedydataViewSet,'comedy')
router.register('children', ChildrendataViewSet,'children')
router.register('crime', CrimedataViewSet,'crime')
router.register('romance', RomancedataViewSet,'romance')
router.register('drama', DramadataViewSet,'drama')
router.register('animation', AnimationdataViewSet,'animation')
router.register('history', HistorydataViewSet,'history')
router.register('mystery', MysterydataViewSet,'mystery')
router.register('war', WardataViewSet,'war')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
