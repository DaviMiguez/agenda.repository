# Generated by Django 2.2.12 on 2020-09-18 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=200, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=10, verbose_name='Cep'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=200, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Contato', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='logradouro',
            field=models.CharField(max_length=200, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Contato', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]