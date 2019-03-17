from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from djangotest.product.models import Product, Operation
from .serializers import ProductSerializer, OperationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    #Campos disponíveis na pesquisa
    filter_fields = ('name',)
    #Se o usuário não estiver logado, ele só podera visualizar
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        queryset = Product.objects.all()
        if name:
            queryset = queryset.filter(name__iexact=name)

        return queryset
'''
    def create(self, request, *args, **kwargs):
        return  super(ProductViewSet, self).create(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        return  super(ProductViewSet, self).list(request, *args, **kwargs)
'''
'''
    @action(methods=['get'], detail=True)
    def algo(self, request, pk=None)
        return pass
'''

class OperationViewSet(ModelViewSet):

    serializer_class = OperationSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('product__name','status',)
    #Limita as requisições HTTP
    http_method_names = ['get', 'post', 'head', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user

        if serializer.is_valid():
            op = Operation.objects.create(**serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            #Se o retorno do create vier com ID nulo, significa que o objeto nao foi criado.
            if op.id != None:
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        #Mensagme de erro que deve ser retornada caso o estoque seja insuficiente
        return Response({
            'status': 'Conflict',
            'message': 'Estoque insuficiente.'
        }, status=status.HTTP_409_CONFLICT)