from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Receita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Receitas'
        verbose_name_plural = 'Receitas'
        db_table = 'receitas'

    def __str__(self):
        return self.nome_receita

    def get_absolute_url(self):
        return reverse('receita', kwargs={'pk': self.id})
