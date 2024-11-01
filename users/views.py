from django.http import HttpResponseBadRequest, JsonResponse
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Parks
# Create your views here.

class getParks(APIView):
    def get(self, request):
        queryset = Parks.objects.all()
        data = serialize('geojson', queryset, geometry_field = 'mpoly', fields = ('id', 'name', 'capacity', 'available_spaces',))
        response = {
            "parks":data,
        }

        return Response(response)


class bookPark(APIView):
    def post(self, request):
        parkid = request.data.get('id')
        print(parkid)
        try:
            park= Parks.objects.get(id=parkid)
            if park.available_spaces - 1 <=0:
                raise Parks.DoesNotExist
            else:
                park.available_spaces -= 1
                if park.booked > park.capacity:
                    raise Parks.DoesNotExist
                park.booked += 1
                park.save()
            return Response({'message':'Parking booked successfully.'})
        except Parks.DoesNotExist:
            return HttpResponseBadRequest(JsonResponse({'message':f'No park with id:{parkid}'}))
        

class freePark(APIView):
    def post(self, request):
        parkid = request.data.get('id')

        try:
            park= Parks.objects.get(id=parkid)
            park.booked -= 1
            park.available_spaces += 1
            park.save()
            return Response({'message':'Parking booked successfully.'})
        except Parks.DoesNotExist:
            return HttpResponseBadRequest(JsonResponse({'message':f'No park with id:{parkid}'}))


