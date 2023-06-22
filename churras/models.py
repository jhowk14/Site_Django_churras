from django.db import models
#from pessoas.models import Pessoa
from django.contrib.auth.models import User
from datetime import datetime
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Prato(models.Model):
    #pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_prato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo =models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_prato = models.DateTimeField(default=datetime.now,blank=True)
    date_prato = models.DateTimeField(default=datetime.now, blank=True) 
    foto_prato = models.ImageField(upload_to=get_file_path, blank=True)
    publicado = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_prato


#python manage.py makemigrations
#python manage.py migrate

