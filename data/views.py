from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QuestionnaireData

# Create your views here.

class UploadData(APIView):
    def post(self, request):
        email = request.POST.get('email')
        id=request.POST.get('id')
        formTitle = request.POST.get('formTitle')
        formStatus= request.POST.get('formStatus')
        datetime= request.POST.get('datetime')
        geometry_type=request.POST.get('geometry_type')
        questions=request.POST.get('questions')
        image_file = request.FILES.get('image_file')
        audio_file = request.FILES.get('audio_file')
        video_file = request.FILES.get('video_file')
        
        try:

            # Create and save the QuestionnaireData object
            questionnaire_data = QuestionnaireData(
                email=email,
                id=id,
                form_title=formTitle,
                form_status=formStatus,
                datetime=datetime,
                geometry_type=geometry_type,
                questions=questions,
                image_file=image_file,
                audio_file=audio_file,
                video_file=video_file,
            )
            questionnaire_data.save()

            # Return success response
            return Response({"message": "Data saved successfully", "id": id}, status=201)

        except Exception as e:
            # Return error response
            return HttpResponseBadRequest(JsonResponse({"error": str(e)}))
        
class EditData(APIView):
    def post(self, request):
        id = request.POST.get('id')  # Required field to identify the object to edit

        try:
            # Fetch the existing QuestionnaireData object
            questionnaire_data = QuestionnaireData.objects.get(id=id)

            # Update fields if provided in the request
            if 'email' in request.POST:
                questionnaire_data.email = request.POST.get('email')
            if 'formTitle' in request.POST:
                questionnaire_data.form_title = request.POST.get('formTitle')
            if 'formStatus' in request.POST:
                questionnaire_data.form_status = request.POST.get('formStatus')
            if 'datetime' in request.POST:
                datetime_str = request.POST.get('datetime')
                questionnaire_data.datetime = datetime_str
            if 'geometry_type' in request.POST:
                questionnaire_data.geometry_type = request.POST.get('geometry_type')
            if 'questions' in request.POST:
                questionnaire_data.questions = request.POST.get('questions')

            # Update files if provided in the request
            if 'image_file' in request.FILES:
                questionnaire_data.image_file = request.FILES.get('image_file')
            if 'audio_file' in request.FILES:
                questionnaire_data.audio_file = request.FILES.get('audio_file')
            if 'video_file' in request.FILES:
                questionnaire_data.video_file = request.FILES.get('video_file')

            # Save the updated object
            questionnaire_data.save()

            # Return success response
            return Response({"message": "Data updated successfully", "id": id}, status=200)

        except QuestionnaireData.DoesNotExist:
            return HttpResponseForbidden(JsonResponse({"error": "QuestionnaireData not found"}))
        except Exception as e:
            # Return error response
            return HttpResponseBadRequest(JsonResponse({"error": str(e)}))
