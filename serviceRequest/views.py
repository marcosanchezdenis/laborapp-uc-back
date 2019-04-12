from rest_framework import viewsets
from serviceRequest.models import *
from serviceRequest.serializers import *


class RequestStateViewSet(viewsets.ModelViewSet):
    queryset = RequestState.objects.all()
    serializer_class = RequestStateSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
""" 
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user=self.request.user)
        return self.queryset """
        

