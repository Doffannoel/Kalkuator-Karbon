from django.db import models

# Create your models here.
class PeralatanListrik(models.Model):
    nama = models.CharField(max_length=100)
    daya = models.FloatField()
    waktu = models.FloatField()

    def __str__(self):
        return self.nama
    
class Sampah(models.Model):
    jenis = models.CharField(max_length=100)
    total = models.FloatField()

    def __str__(self):
        return self.jenis
    
class BahanBakar(models.Model):
    jenis = models.CharField(max_length=100)
    total = models.FloatField()

    def __str__(self):
        return self.jenis
    

