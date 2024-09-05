import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import ComplexField, SearchIndex, SearchFieldDataType, SimpleField, SearchableField
from dotenv import load_dotenv

load_dotenv()

SEARCH_SERVICE_NAME = os.getenv('SEARCH_SERVICE_NAME')
SEARCH_SERVICE_KEY = os.getenv('SEARCH_SERVICE_KEY')
SEARCH_INDEX_NAME = os.getenv('SEARCH_INDEX_NAME')

endpoint = f"https://{SEARCH_SERVICE_NAME}.search.windows.net"
credential = AzureKeyCredential(SEARCH_SERVICE_KEY)
index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
search_client = SearchClient(endpoint=endpoint, credential=credential, index_name=SEARCH_INDEX_NAME)

def create_index():
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="name", type=SearchFieldDataType.String, searchable=True, filterable=True),
        SearchableField(name="description", type=SearchFieldDataType.String, searchable=True),
        SimpleField(name="price", type=SearchFieldDataType.Double, filterable=True, sortable=True),
        SearchableField(name="category", type=SearchFieldDataType.String, filterable=True)
    ]

    index = SearchIndex(name=SEARCH_INDEX_NAME, fields=fields)
    result = index_client.create_index(index)
    print(f"Índice Criado: {result.name}")

def upload_documents():
    documents = [
        {"id": "1", "name": "Laptop", "description": "A high performance laptop", "price": 1500.0, "category": "Electronics"},
        {"id": "2", "name": "Coffee Maker", "description": "A coffee maker with timer", "price": 50.0, "category": "Home Appliances"},
        {"id": "3", "name": "Headphones", "description": "Noise-cancelling headphones", "price": 200.0, "category": "Electronics"}
    ]

    result = search_client.upload_documents(documents=documents)
    print(f"Documentos carregados: {result}")

def search_documents():
    search_term = "timer"
    filter_expression = "category eq 'Electronics'"
    results = search_client.search(
        # search_text=search_term,
        filter=filter_expression
    )

    for result in results:
        print(result)
        print(f"ID: {result['id']}, Name: {result['name']}, Description: {result['description']}, Price: {result['price']}, Category: {result['category']}")


# create_index()
# upload_documents()
search_documents()