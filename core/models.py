from django.db import models
# from django.contrib.auth.models import User
import requests



class Contato(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    contato = models.ForeignKey(Contato, on_delete=models.PROTECT)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=200, verbose_name='rua')
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    contato = models.ForeignKey(Contato, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.contato}'

    def consulta_cep(self, cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.request("GET", url)
        return response

    def save(self, *args, **kwargs):
        response = self.consulta_cep(self.cep)
        dados_cep = response.json()
        self.cidade = dados_cep.get('localidade')
        self.logradouro = dados_cep.get('logradouro')
        self.bairro = dados_cep.get('bairro')
        super(Endereco, self).save(*args, **kwargs)
