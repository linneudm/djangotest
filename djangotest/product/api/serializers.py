from rest_framework.serializers import ModelSerializer, ValidationError
from djangotest.product.models import Product, Operation


class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'picture', 'price', 'quantity')

class OperationSerializer(ModelSerializer):
	class Meta:
		model = Operation
		fields = ('id', 'user', 'product', 'created_on', 'status', 'quantity')
#product = ProductSerializer()
'''
	def validate(self, data):
		if data['product_quantity'] < data['quantity']:
			raise ValidationError('Sem estoque suficiente!')
'''