from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cities, Subscriptions


class CityListView(ListView):
    model = Cities
    template_name = 'configurations/city_list.html'


class CityCreateView(CreateView):
    model = Cities
    fields = ['city']
    template_name = 'configurations/city_form.html'
    success_url = reverse_lazy('configurations:city_list')


class CityUpdateView(UpdateView):
    model = Cities
    fields = ['city']
    template_name = 'configurations/city_form.html'
    success_url = reverse_lazy('configurations:city_list')


class CityDeleteView(DeleteView):
    model = Cities
    template_name = 'configurations/city_confirm_delete.html'
    success_url = reverse_lazy('configurations:city_list')


class SubscriptionListView(ListView):
    model = Subscriptions
    template_name = 'configurations/subscription_list.html'
    context_object_name = 'subscriptions'

class SubscriptionCreateView(CreateView):
    model = Subscriptions
    fields = ['subscription']
    template_name = 'configurations/subscription_form.html'
    success_url = reverse_lazy('configurations:subscription_list')


class SubscriptionUpdateView(UpdateView):
    model = Subscriptions
    fields = ['subscription']
    template_name = 'configurations/subscription_form.html'
    success_url = reverse_lazy('configurations:subscription_list')


class SubscriptionDeleteView(DeleteView):
    model = Subscriptions
    template_name = 'configurations/subscription_confirm_delete.html'
    success_url = reverse_lazy('configurations:subscription_list')
