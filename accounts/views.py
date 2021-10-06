from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def index(request):
    return HttpResponse('hello')