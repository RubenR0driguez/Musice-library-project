from rest_framework import serializers
from .models import Music

class musicserializer(serializers.ModelSerializer):
    class meta:
        model = Music
        fields = ['id','title','artist','album','release_date','genre' ]