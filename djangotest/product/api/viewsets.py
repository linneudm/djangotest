from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from djangotest.product.models import Product, Operation
from .serializers import ProductSerializer, OperationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class ProductViewSet(ModelViewSet):

    #queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('name',)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
    	name = self.request.query_params.get('name', None)
    	queryset = Product.objects.all()
    	if name:
    		queryset = queryset.filter(name__iexact=name)

    	return queryset

    def create(self, request, *args, **kwargs):
    	return	super(ProductViewSet, self).create(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
    	return	super(ProductViewSet, self).list(request, *args, **kwargs)
'''
	@action(methods=['get'], detail=True)
	def algo(self, request, pk=None)
		return pass
'''

class OperationViewSet(ModelViewSet):

    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('product__name','status',)
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = [IsAccountAdminOrReadOnly]

    def validate_entry(self, product, quantity, operation):
        if(operation == "Saída" and int(quantity) > product.quantity):
            return True
        else:
            return False

    def create(self, request, *args, **kwargs):
        id_p = request.data['product']
        product = Product.objects.get(id=id_p)
        qtd = request.data['quantity']
        operation = request.data['status']
        if(self.validate_entry(product, qtd, operation)):
            error = {'message': "Estoque insuficiente. Não foi possível realizar a operação."}
            raise ValidationError(error)
        else:
            if (operation == "Saída"):
                product.quantity -= int(qtd)
            else:
                product.quantity += int(qtd)
            product.save()
            return super(OperationViewSet, self).create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        id_p = request.data['product']
        product = Product.objects.get(id=id_p)
        qtd = request.data['quantity']
        operation = request.data['status']
        if(self.validate_entry(product.quantity, qtd, operation)):
            error = {'message': "Estoque insuficiente. Não foi possível realizar a operação."}
            raise ValidationError(error)
        else:
            if (operation == "Saída"):
                product.quantity -= int(qtd)
            else:
                product.quantity += int(qtd)
            product.save()
            return super(OperationViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        id_p = request.data['product']
        product = Product.objects.get(id=id_p)
        qtd = request.data['quantity']
        operation = request.data['status']
        if(self.validate_entry(product.quantity, qtd, operation)):
            error = {'message': "Estoque insuficiente. Não foi possível realizar a operação."}
            raise ValidationError(error)
        else:
            if (operation == "Saída"):
                product.quantity -= int(qtd)
            else:
                product.quantity += int(qtd)
            product.save()
            return super(OperationViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        id_p = obj.product.pk
        product = Product.objects.get(id=id_p)
        qtd = obj.quantity
        operation = obj.status
        if(operation == "Saída"):
            product.quantity += int(qtd)
        else:
            product.quantity -= int(qtd)
        product.save()
        return super(OperationViewSet, self).destroy(request, *args, **kwargs)
'''
    def get_queryset(self):
    	status = self.request.query_params.get('status', None)
    	
    	queryset = Operation.objects.all()
    	if status:
    		queryset = queryset.filter(status__iexact=status)

    	return queryset
'''