from django.db import models

class ProductManager(models.Manager):
    def search(self, query):
        return self._queryset().filter(
            models.Q(name__icontains=query)
        )

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    amount = models.IntegerField('Quantidade')
    weight = models.DecimalField('Peso', max_digits=10, decimal_places=5)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
