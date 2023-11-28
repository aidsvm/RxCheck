import requests
from bs4 import BeautifulSoup
import sys

print(sys.path)


def get_drug_interactions(drug_name):
    base_url = 'https://www.drugs.com/drug-interactions/'
    user_selected_url = f'{base_url}{drug_name.lower()}-index.html'

    response = requests.get(user_selected_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        drug_list = soup.find_all('ul',
                                  class_='interactions ddc-list-column-2')  # Find all 'ul' elements containing drug info
        if drug_list:
            print(f"Interactions for {drug_name}:")
            for ul_element in drug_list:
                li_elements = ul_element.find_all('li')
                if li_elements:
                    for li in li_elements:
                        item_content = li.text
                        print(item_content.strip())
                else:
                    print(f"No interactions found for {drug_name}.")
        else:
            print(f"No drugs/interactions found for {drug_name}.")
    else:
        print(f"Failed to retrieve data for {drug_name}. Please check the drug name.")


def get_drug_info(drug_name):
    base_url = 'https://www.drugs.com/'
    user_selected_url = f'{base_url}{drug_name.lower()}.html'

    response = requests.get(user_selected_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    info_heading = soup.find('h2', id='uses')

    if info_heading:
        p_elements = info_heading.find_next('p')
        drug_info = p_elements.text
        print(drug_info.strip())


