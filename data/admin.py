from django.contrib import admin
from .models import QuestionnaireData
# Register your models here.

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display=['id','email','form_title', 'form_status', 'datetime', 'geometry_type','image_file','audio_file', 'video_file',]
    
admin.site.register(QuestionnaireData, QuestionnaireAdmin)
