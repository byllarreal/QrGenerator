from rest_framework import serializers
from .models import qrgenerModel

class qrgenerSerializer(serializers.ModelSerializer):
    class Meta:
        model=qrgenerModel
        fields='__all__'



