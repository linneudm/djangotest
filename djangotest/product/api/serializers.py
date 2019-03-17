from rest_framework.serializers import ModelSerializer, ValidationError
from djangotest.product.models import Product, Operation


#Serialização dos dados
class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'picture', 'price', 'quantity')

class OperationSerializer(ModelSerializer):
	class Meta:
		model = Operation
		fields = ('id', 'product', 'created_on', 'status', 'quantity')