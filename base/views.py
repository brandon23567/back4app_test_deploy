from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UploadNewImage

@api_view(["GET"])
def index(request):
    return Response({"message": "this is the index page"})


@api_view(["POST"])
def add_new_image(request):
    image_caption = request.data.get("imageCaption")
    image = request.FILES.get("imageFile")
    
    new_image = UploadNewImage.objects.create(image_caption=image_caption, image=image)
    new_image.save()
    
    return Response({"message": "image has been uploaded to backend"})


@api_view(["GET"])
def get_all_posts(request):
    images_in_db = UploadNewImage.objects.all()
    images_array = []
    
    for image in images_in_db:
        single_image_data = {
            "image_caption": image.image_caption,
            "actual_image_url": image.image.url
        }
        
        images_array.append(single_image_data)
        
    return Response(images_array)