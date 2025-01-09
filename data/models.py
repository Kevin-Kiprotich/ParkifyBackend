from django.db import models

# Create your models here.

class QuestionnaireData(models.Model):
    id=models.CharField(max_length=1000, primary_key=True)
    email=models.EmailField(null=False)
    form_title = models.CharField(max_length=40, null=False)
    form_status = models.CharField(max_length=40, null=False, default="submitted")
    datetime=models.CharField(max_length=200, null=False)
    questions=models.TextField(null=False)
    geometry_type=models.CharField(max_length=40, null=True)
    image_file=models.ImageField(upload_to='Images',null=True)
    audio_file=models.FileField(upload_to="Audio",null=True)
    video_file=models.FileField(upload_to="Videos", null=True)
    
    class Meta:
        verbose_name_plural="Questionnaire Data"
