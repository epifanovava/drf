from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet, basename='women')  #если мы убираем queryset


#Определим свой класс Router (его лучше определять в отдельном файле router.py)
class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-list',
                      detail=True,
                      initkwargs={'suffix': 'retrieve'})

    ]


router = MyCustomRouter()
router.register(r'women', WomenViewSet, basename='women')  #если мы убираем queryset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  #http://127.0.0.1:8000/api/v1/women.
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update '})),
]




