from audioop import reverse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Sodas
from django.views.generic import DetailView


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


# class Sodas:
#     def __init__(self, name, img, flavor):
#         self.name = name
#         self.img = img
#         self.flavor = flavor
# sodas = [
#     Sodas('Fanta', 'https://www.fanta.com/content/dam/nagbrands/us/fanta/en/products/orange/desktop/Orange_Bottle_Desktop.png', 'Orange'),
#     Sodas('Pepsi', 'https://www.meijer.com/content/dam/meijer/product/0001/20/0000/12/0001200000129_1_A1C1_0600.png', 'Original'),
#     Sodas('Coke', 'data:image/jpeg;base64,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', 'Cherry'),
#     Sodas('Dr Pepper', 'https://i.imgur.com/BtC2I2tb.jpg','Original'),
#     Sodas('A&W', 'https://i.imgur.com/A0ZJmmEb.jpg', 'Root beer')


# ]

class SodaList(TemplateView):
    template_name = 'soda_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sodas'] = Sodas.objects.all()

        return context


class SodaCreate(CreateView):
    model= Sodas
    fields = ['name', 'img', 'flavor']
    template_name = "sodas_create.html"
    def get_success_url(self):
        return reverse('soda_detail', kwargs={'pk: self.object.pk'})




class SodaUpdate(UpdateView):
    model = Sodas
    fields = ['name', 'img', 'flavor']
    template_name = 'soda_update.html'
    
    def get_success_url(self):
        return reverse('soda_detail', kwargs={'pk': self.object.pk})


class SodaDelete(DeleteView):
    model = Sodas
    template_name = 'sodas_delete_confirmation.html'
    success_url = '/sodas/'
