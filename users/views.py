from django.http import HttpResponseBadRequest, JsonResponse
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Parks,ParkingSlots
# Create your views here.

class getParks(APIView):
    def get(self, request):
        queryset = ParkingSlots.objects.all()
        data = serialize('geojson', queryset, geometry_field = 'geometry', fields = ('id', 'name','slot_no','is_parked',))
        response = {
            "slots":data,
        }

        return Response(response)


class bookPark(APIView):
    def post(self, request):
        slotID = request.data.get('id')
        
        try:
            slot= ParkingSlots.objects.get(id=slotID)
            if slot.is_parked:
                return HttpResponseBadRequest(JsonResponse({'message':f"{slot.id} is already taken"}))
            else:
                slot.is_parked = True
                slot.save()
                return Response({'message':'Parking booked successfully.'})
        except ParkingSlots.DoesNotExist:
            return HttpResponseBadRequest(JsonResponse({'message':f'No parking slot with id:{slotID}'}))
        

class freePark(APIView):
    def post(self, request):
        slotID = request.data.get('id')

        try:
            slot= ParkingSlots.objects.get(id=slotID)
            slot.is_parked = False
            slot.save()
            return Response({'message':'Parking booked successfully.'})
        except Parks.DoesNotExist:
            return HttpResponseBadRequest(JsonResponse({'message':f'No parking slot with id:{slotID}'}))


