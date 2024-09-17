from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from qrgener import views

router=routers.DefaultRouter()
router.register('qrgener',views.qrgenerView, 'qrgener')

urlpatterns=[
    path('api/v1/', include(router.urls)),
    path('Docs/', include_docs_urls(title='QR Generator API')),
]
