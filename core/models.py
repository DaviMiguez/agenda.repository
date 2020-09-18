from django.db import models
# from django.contrib.auth.models import User
import requests



class Contato(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    telefone = models.CharField(max_length=11, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')
    contato = models.ForeignKey(Contato, on_delete=models.PROTECT, verbose_name='Contato')
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

class Endereco(models.Model):
    cep = models.CharField(max_length=10, verbose_name='Cep')
    logradouro = models.CharField(max_length=200, verbose_name='Rua')
    bairro = models.CharField(max_length=200, verbose_name='Bairro')
    cidade = models.CharField(max_length=200, verbose_name='Cidade')
    contato = models.ForeignKey(Contato, on_delete=models.PROTECT, verbose_name='Contato')

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
