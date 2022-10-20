from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_token(request):
    return Response({
        'username': request.user.username,
        'frist_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'is_staff': request.user.is_staff
    }, status=status.HTTP_200_OK)
