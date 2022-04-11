from rest_framework import serializers
from .models import *

class GetHX(serializers.ModelSerializer):
    class Meta:
        model = HX
        fields = ('Tcin', 'Tcout', 'Thin', 'Thout', 'Fhot', 'Fcold', 'Tsetpt')
