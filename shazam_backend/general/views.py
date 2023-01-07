from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from general.serializers import SiteInfoSerializer
from general.models import SiteInfo


class Site(APIView):
    def get(self, request):
        site_info, _ = SiteInfo.objects.get_or_create(pk=1)
        site = SiteInfoSerializer(site_info)
        return Response(site.data)

    @permission_classes([IsAuthenticated, IsAdminUser])
    def put(self, request):
        site_info, _ = SiteInfo.objects.get_or_create(pk=1)
        site = SiteInfoSerializer(site_info, data=request.data, partial=True)
        if site.is_valid():
            site.save()
            return Response(site.data)
        return Response(site.errors)
