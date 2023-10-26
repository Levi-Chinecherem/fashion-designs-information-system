# designs/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Design(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='designs/cover_images/')
    content = RichTextUploadingField()
    designer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.TextField()

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
