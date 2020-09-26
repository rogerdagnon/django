from django.db import models


# Create your models here.
class Topico(models.Model):
    nome = models.CharField(max_length=264, unique=True)#chave primaria


    def __str__(self):
        return self.nome                                     #padrao de str para mostrar no admin

class Webpage(models.Model):                                     #classes de python representando modelos de dados
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE) #Chave estrangeira - on_delete cascade para apagar tbm os acessos
    nome = models.CharField(max_length=264, unique=True)         #Um campo string, para campos texto de tamanhos pequeno e médio e unico
    url = models.URLField(unique=True)                           #um CharField com validador de URL e unico

    def __str__(self):
        return self.nome

class RegistroAcesso(models.Model):
    pagina = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    data = models.DateField()                                    #uma data em formato padrao

    def __str__(self):
        return str(self.data)

class Model(models.Model):
    nome = models.CharField(max_length=264, unique=True)         #chave primaria

    def __str__(self):
        return self.nome                                         #padrao de str para mostrar no admin

class DadosForm(models.Model):
    nome = models.CharField(max_length=264, unique=True)         #chave primaria
    email = models.EmailField(max_length=264, unique=True)
    texto = models.CharField(max_length=264, unique=True)
    endereco = models.CharField(max_length=264, unique=True)
    cidade = models.CharField(max_length=264, unique=True)


    def __str__(self):
        return self.nome                                         #padrao de str para mostrar no admin