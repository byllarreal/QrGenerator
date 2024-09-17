from django.db import models

# Create your models here.
class qrgenerModel(models.Model):
    url=models.URLField(null=True, blank=True)
    descripcion=models.TextField()
    vcard=models.TextField()
    email=models.EmailField()
    telefono=models.CharField(max_length=15)
    wifi=models.TextField(null=True, blank=True)
    geo=models.CharField(max_length=100, null=True, blank=True)
    img_qr=models.ImageField(upload_to='qrs/', null=True, blank=True)

    def __str__(self):
        return f"QR Data: {self.url or self.descripcion or 'Sin datos'}"
