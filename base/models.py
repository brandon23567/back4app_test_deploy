from django.db import models
from cloudinary.models import CloudinaryField

class UploadNewImage(models.Model):
    image_caption = models.CharField(max_length=200)
    image = CloudinaryField(resource_type="image", folder="test_Images/")
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.image_caption
