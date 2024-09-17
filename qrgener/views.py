from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializer import qrgenerSerializer
from .models import qrgenerModel
from .QrCoding import QrCoding

# Create your views here.
class qrgenerView(viewsets.ModelViewSet):
    serializer_class=qrgenerSerializer
    queryset=qrgenerModel.objects.all()


    @action(detail=True, methods=['post'])
    def gener_qr(self, request, pk=None):
        qrcoding=QrCoding()
        qr_data=self.get_object()
        img_fiel=qrcoding.qrcod(qr_data)
        qr_data.img_qr.save(img_fiel.name, img_fiel)
        qr_data.save()
        return Response({"status":"QR generado y guardado con éxito", "qr_data_id":qr_data.id}, status=status.HTTP_200_OK)

    
    
