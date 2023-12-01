from django.shortcuts import render, redirect
from .models import Drug, Drug_History
from django.http import JsonResponse
from .utils import get_drug_interactions, get_drug_info
from .forms import DrugSearchForm


def search_drug(request):
    if request.method == 'POST':
        form = DrugSearchForm(request.POST)
        if form.is_valid():
            drug_name = form.cleaned_data['drug_name']
            drug_interactions = get_drug_interactions(drug_name)
            drug_info = get_drug_info(drug_name)
            return render(request, 'search_results.html', {'drug_name': drug_name,
                                                           'info': drug_info, 'interactions': drug_interactions})
    else:
        form = DrugSearchForm()
    return render(request, 'search_drug.html', {'form': form})


def search_results(request, drug_name, interactions):
    context = {
        'drug_name': drug_name,
        'interactions': interactions,
    }
    return render(request, 'search_results.html', context=context)


def login_page(request):
    # Your logic for the login page
    return render(request, 'login_page.html')


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_drugs = Drug.objects.all().count()
    num_history = Drug_History.objects.all().count()

    context = {
        'drugs': num_drugs,
        'num_history': num_history,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
