from django.db import models


# Create your models here.

class UserRoles(models.TextChoices):
    ADMINISTRADOR_SISTEMA = 'Administrador Sistema'
    GERENTE_ACADEMIA = 'Administrador Academia'
    FUNCIONARIO_ACADEMIA = 'Funcionário Academia'
    CLIENTE_ACADEMIA = 'Cliente Academia'


class Usuario(models.Model):
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=UserRoles.choices)
    academy_id = models.PositiveSmallIntegerField()

