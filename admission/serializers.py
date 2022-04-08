from rest_framework import routers, serializers, viewsets
from admission.models import Admission

class AddmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'
        # exclude = 'id'
