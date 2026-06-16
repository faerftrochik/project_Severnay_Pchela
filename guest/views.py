from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from guest.models import Guest


class GuestCreateView(SuccessMessageMixin,
                        CreateView):
    model = Guest
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Гость добавлен."

class GuestUpdateView(SuccessMessageMixin,
                          UpdateView):
    model = Guest
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Гость обновлен."

