from django.db import models
from django.contrib.auth.models import User

class UserPortView(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    port = models.ForeignKey('Port', on_delete=models.CASCADE)
    custom_name = models.CharField(max_length=100)
        
class UserPortGroup(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    port_group = models.ManyToManyField('Port', blank=True)

class Device(models.Model):
    mac = models.CharField(max_length=17)
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class Port(models.Model):
    PORT_CHOICES = [
        ('NIVEL', 'Nível de Água'),
        ('FLUXO', 'Fluxo de Água'),
    ]
    port_number = models.IntegerField()
    port_type = models.CharField(
        max_length=10, 
        choices=PORT_CHOICES
    )
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    config = models.JSONField(blank=True, null=True)

class DataPort(models.Model):
    time_stamp = models.DateTimeField()
    value = models.FloatField()
    std = models.FloatField()
    port = models.ForeignKey('Port', on_delete=models.CASCADE)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    func = models.CharField(max_length=100)

class Conta(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    expiration = models.DateField()
    list_port = models.ManyToManyField('Port', blank=True)


class Alert(models.Model):
    ALERT_CHOICES = [
        ('VAZAMENTO','Vazamento'),
        ('SOBRECONSUMO','Sobreconsumo'),
        ('FORA DO PADRÃO','Fora do padrão')
    ]
    alert_type = models.CharField(
        max_length=100,
        choices=ALERT_CHOICES
    )
    title = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=180)


    


