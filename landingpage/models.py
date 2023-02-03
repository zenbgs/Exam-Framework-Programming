from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length = 50)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=(models.DateTimeField(auto_now_add=True))
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

class Transaksi(models.Model):
    kodetrans=models.CharField(max_length=10)
    tgltrans=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()

class JenisTanaman(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Tanaman(models.Model):
    kodetanaman=models.CharField(max_length = 50)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link=models.CharField(max_length=150, blank=True)
    jenis_id=models.ForeignKey(JenisTanaman, on_delete=models.CASCADE,null=True)


