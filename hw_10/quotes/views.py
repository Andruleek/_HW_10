from django.shortcuts import render
from .utils import get_mongodb
from django.core.paginator import Paginator

def main(request):
    db = get_mongodb()
    quotes = list(db.quotes.find())
    per_page = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def home_view(request):
    return render(request, 'quotes/home.html')

