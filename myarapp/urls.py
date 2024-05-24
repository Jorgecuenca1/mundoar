from django.urls import path
from .views import ARSceneView, indexView

urlpatterns = [
    path('ar', ARSceneView.as_view(), name='ar_scene'),
    path('', indexView.as_view(), name='index'),
]
