from django.shortcuts import render
from django.views import View

# Create your views here.
class Delivery(View):
    def delivery(self, request):
        try:
            