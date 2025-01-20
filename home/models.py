# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cidade(models.Model):

    #__Cidade_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    uf = models.CharField(max_length=255, null=True, blank=True)
    ibge = models.CharField(max_length=255, null=True, blank=True)
    situacao = models.BooleanField()

    #__Cidade_FIELDS__END

    class Meta:
        verbose_name        = _("Cidade")
        verbose_name_plural = _("Cidade")


class Colaborador(models.Model):

    #__Colaborador_FIELDS__
    apelido = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cep = models.CharField(max_length=255, null=True, blank=True)
    id_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    e-mail = models.CharField(max_length=255, null=True, blank=True)
    situacao = models.BooleanField()

    #__Colaborador_FIELDS__END

    class Meta:
        verbose_name        = _("Colaborador")
        verbose_name_plural = _("Colaborador")



#__MODELS__END
