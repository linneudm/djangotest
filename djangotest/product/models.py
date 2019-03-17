from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField('Nome', max_length=250, null=False, blank=False)
	picture = models.ImageField('Ilustração', upload_to="poducts", null = True, blank = True)
	price = models.DecimalField('Preco Unitário', max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField('Quantidade', default=0)

	def __str__(self):
		return self.name

class Operation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	INPUT = 'Entrada'
	OUTPUT  = 'Saída'
	STATUS_CHOICES = ((INPUT, 'Entrada'), (OUTPUT, 'Saída'),)
	status = models.CharField('Operação', max_length=10, choices=STATUS_CHOICES, default=INPUT)
	quantity = models.PositiveIntegerField('Quantidade', default=0)

	#Funcao que retorna o custo total da operacao
	def total_price(self):
		return self.product.price * self.quantity

	#Funcao que define uma string pra cada operacao pra facilitar a visualizacao
	def __str__(self):
		name = (self.status + " - " + (self.created_on.strftime("%d/%m/%Y às %H:%M:%S")))
		return name

	#Verifica o estoque do produto antes de fazer a retirada do mesmo para entao efetuar o save.
	def delete(self, *args, **kwargs):
		product = Product.objects.get(id=self.product.id)
		if(self.status == "Saída"):
			status = True
		else:
			status = False
			
		if(status):
			product.quantity += self.quantity
		else:
			product.quantity -= self.quantity
		product.save()
		super(Operation, self).delete(*args, **kwargs)

	def save(self, *args, **kwargs):
		product = Product.objects.get(id=self.product.id)
		if(self.status == "Saída"):
			status = True
		else:
			status = False
		if(self.quantity > product.quantity and status):
			return None
		else:
			if(status):
				product.quantity -= self.quantity
			else:
				product.quantity += self.quantity
			product.save()
			super(Operation, self).save(*args, **kwargs)