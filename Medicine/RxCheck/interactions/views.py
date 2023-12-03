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


def compare_drugs(request):
    if request.method == "POST":
        drug1 = request.POST.get('drug1', '')
        drug2 = request.POST.get('drug2', '')

        if not drug1 and not drug2:
            return render(request, 'error.html', {'error_message':
                                                      'Please provide valid drug names.'})
        drug1_interactions = set(get_drug_interactions(drug1))

        if drug1_interactions.intersection([drug2]):
            result_message = f"{drug2} interacts with {drug1}."
        else:
            result_message = f"{drug2} does not interact with {drug1}."

        return render(request, 'search_results.html', {'compare': result_message})

    # If the request method is not POST, render the initial form
    return render(request, 'compare_drugs.html')


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
