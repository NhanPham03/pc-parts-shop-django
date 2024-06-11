from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

client = MongoClient(
  host=settings.DATABASES['default']['CLIENT']['host'],
  username=settings.DATABASES['default']['CLIENT']['username'],
  password=settings.DATABASES['default']['CLIENT']['password']
)
db = client[settings.MONGODB_NAME]
collection = db[Product._meta.db_table]

collection.create_index([
  ('name', 'text'),
  ('type', 'text')
])

@api_view(['GET'])
def ProductSearch(request, q):
  if request.method == 'GET':
    try:
      results = collection.find({'$text': {'$search': q}})
      results_list = [dict(result) for result in results]
      
      for result in results_list:
        result['_id'] = str(result['_id'])

      serializer = ProductSerializer(results_list, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
