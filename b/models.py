from django.db import models

# Create your models here
    
class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=70)
    message = models.TextField()

    class Meta:
        app_label = 'contacts'

    def __str__(self):
        return self.name