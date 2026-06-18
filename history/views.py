from django.shortcuts import render

from django.views.generic import ListView

from history.models import History


class HistoryGuestView(ListView):
    model = History

    def get_queryset(self):
        qs = super().get_queryset().filter(guest_pk=self.kwargs["pk"])
        return qs
