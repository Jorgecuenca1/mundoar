from django.urls import path
from .views import (
    ARSceneView, indexView, whychooseView, contactView, aboutView,
    itserviceView, managedserviceView, industriesView, businessView, servicedetailView
)

urlpatterns = [
    path('ar', ARSceneView.as_view(), name='ar_scene'),
    path('nosotros', aboutView.as_view(), name='about'),
    path('contacto', contactView.as_view(), name='contact'),
    path('eligenos', whychooseView.as_view(), name='whychoose'),
    path('', indexView.as_view(), name='index'),
    path('it-services', itserviceView.as_view(), name='it-services'),
    path('managed-it-service', managedserviceView.as_view(), name='managed-it-service'),
    path('industries', industriesView.as_view(), name='industries'),
    path('business-solution', businessView.as_view(), name='business-solution'),
    path('it-services-details', servicedetailView.as_view(), name='it-services-details'),
]
