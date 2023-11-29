from django.shortcuts import render, redirect
from .models import Drug, Drug_History
from django.http import JsonResponse
from .utils import get_drug_interactions


def search_drug(request):
    if request.method == 'POST':
        drug_name = request.POST.get('drugName')

        # Call your BeautifulSoup scraping functions and get the drug interactions or information
        drug_interactions = get_drug_interactions(drug_name)  # Modify this line based on your scraper code

        print(f"Redirecting to search_results with drug_name: {drug_name}, interactions: {drug_interactions}")

        # Redirect to the search_results page with the drug interactions
        return redirect('search_results', drug_name=drug_name, interactions=drug_interactions)

    # Handle cases where the request method is not POST
    return JsonResponse({'error': 'Invalid request method'})


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
