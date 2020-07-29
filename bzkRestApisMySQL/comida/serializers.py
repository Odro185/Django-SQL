from rest_framework import serializers 
from comida.models import comida
 
 
class comidaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = comida
        fields = ('id',
                  'title',
                  'description',
                  'published')
