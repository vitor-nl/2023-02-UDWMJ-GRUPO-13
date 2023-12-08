from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='static/img/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
   
    def __str__(self) -> str:
        return self.nome

    def get_display_price(self):
        return self.preco