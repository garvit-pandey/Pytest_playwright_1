import requests
import pprint   # this module is to convert JSON data into readble format
import pytest


# Get request

url1 = 'https://api.nationalize.io/?name=nathaniel'
url2= 'https://bored-api.appbrewery.com/random'
url3 = 'https://api.restful-api.dev/objects/6'
url4 = "https://dummyjson.com/quotes"


# Post request

Purl1 = 'https://api.restful-api.dev/objects'

# Query params
query_param = {"country_id":"GB","probability":0.054157}
target_country = "GB"
extracted_data = None

target_id = 10
expected_result = None


@pytest.mark.skip
def test_get_API():

    get_response = requests.get(url1, params=query_param)
    assert get_response.status_code == 200
    data = get_response.json()
    print('API response fetched: ' + str(data))

    for item in data['country']:
        if item['country_id'] == target_country:
            extracted_data = item
            break

    # 3. Use pytest assertions to verify the data exists and is correct
    assert extracted_data is not None, f"Country '{target_country}' was not found in the response."
    assert extracted_data['probability'] > 0, "Probability should be greater than 0."
    
    print(f"Successfully extracted: {extracted_data}")
    pprint.pprint(data)


@pytest.mark.skip
def test_get_any_api_response():
    get_response = requests.get(url4)
    data1 = get_response.json()
    pprint.pprint(data1)

    for item in data1['quotes']:
        if item['id'] == target_id:
            expected_result = item

    print(f'this is expected output: {expected_result}')



@pytest.mark.skip
def test_post_api():

    post_data = {

    "name": "Dell Inspiron 7",
    "data": {
    "year": 2026,
    "price": 67000,
    "CPU model": "Intel Core i5",
    "Hard disk size": "512 GB"
    }}

    postResponse = requests.post(Purl1, json=post_data)
    print('Posted the response: ' + str(postResponse.json()))

    assert postResponse.status_code == 201

