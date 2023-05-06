from django.db import models
from ckeditor.fields import RichTextField
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    service = models.CharField(max_length=100)
    date_requested = models.DateTimeField(auto_now_add=True)
    
class LatestProject(models.Model):
    feature_image=models.ImageField(upload_to="LatestProject/feature_image", help_text='image size must should be 601 X 399 px & 583 X 583 Px')
    project_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    project_start_date=models.CharField(max_length=100)
    project_end_date=models.CharField(max_length=100)
    about_the_project=RichTextField()
    def __str__(self):
        return self.project_name
    
class ProjectImage(models.Model):
    project_name=models.ForeignKey(LatestProject, on_delete=models.CASCADE)
    project_images=models.ImageField(upload_to="LatestProject/Project-Image", help_text='image size must should be 1200 X 650 px')