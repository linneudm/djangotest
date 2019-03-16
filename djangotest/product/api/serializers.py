from rest_framework.serializers import ModelSerializer
from djangotest.product.models import Product, Operation


class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'picture', 'price', 'quantity')

class OperationSerializer(ModelSerializer):
	product = ProductSerializer()
	class Meta:
		model = Operation
		fields = ('id', 'user', 'product', 'created_on', 'status', 'quantity')