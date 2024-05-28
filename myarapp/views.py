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

class aboutView(View):
    template_name = 'mintech/about-us-01.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class contactView(View):
    template_name = 'mintech/contact-us.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class whychooseView(View):
    template_name = 'mintech/why-choose-us.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class itserviceView(View):
    template_name = 'mintech/it-services.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
class managedserviceView(View):
    template_name = 'mintech/managed-it-service.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class industriesView(View):
    template_name = 'mintech/industries.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
class businessView(View):
    template_name = 'mintech/business-solution.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class servicedetailView(View):
    template_name = 'mintech/it-services-details.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
