from django.shortcuts import render
from .models import Drug, Drug_History
from django.http import JsonResponse
from .utils import get_drug_interactions


# Now you can use functions/classes from utils module


def search_drug(request):
    drug_name = request.POST.get('drug_name')

    # Call your BeautifulSoup scraping functions and get the drug interactions or information
    drug_interactions = get_drug_interactions(drug_name)  # Modify this line based on your scraper code
    # Or call scraper.get_drug_info(drug_name) for drug information
    # Return the response as JSON
    response_data = {
        'interactions': drug_interactions,
    }
    return JsonResponse(response_data)


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
