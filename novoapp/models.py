from django.db import models

# Create your models here.
class Filme(models.Model):
    genero_acao ='GA'
    genero_terror ='GT'
    genero_aventura = 'GV'
    genero_comedia = 'GC'
    genero_opcoes=[
        (genero_acao,'Ação'),
        (genero_terror,'Terror'),
        (genero_aventura,'Aventura'),
        (genero_comedia,'Comédia'),
    ]
    
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=2,choices=genero_opcoes,default=genero_acao)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.PositiveIntegerField()
    classificacao_indicativa = models.PositiveIntegerField()
    cartaz = models.ImageField(upload_to= 'media')

    def __str__(self):
        return self.nome