from django.db import models

from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser): 
    data_nascimento = models.fields.DateField("Data de Nascimento", null=True, blank=True)
    cpf = models.CharField("CPF", max_length=11, null=True, blank=True)


