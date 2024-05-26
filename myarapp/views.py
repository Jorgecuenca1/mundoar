from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

class ARSceneView(View):
    template_name = 'myarapp/ar_scene.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class indexView(View):
    template_name = 'mintech/index-software-innovation.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
