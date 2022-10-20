from rest_framework.response import Response
from rest_framework.views import APIView
from general.serializers import SiteInfoSerializer
from general.models import SiteInfo


class Site(APIView):
    def get(self, request):
        site = SiteInfoSerializer(SiteInfo.objects.get(pk=1))
        return Response(site.data)
