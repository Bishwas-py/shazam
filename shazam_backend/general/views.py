from rest_framework.response import Response
from rest_framework.views import APIView
from general.serializers import SiteInfoSerializer
from general.models import SiteInfo


class Site(APIView):
    def get(self, request):
        site_info, _ = SiteInfo.objects.get_or_create(pk=1)
        site = SiteInfoSerializer(site_info)
        return Response(site.data)
