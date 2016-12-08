
from rest_framework import serializers
from films.models import *

class HomelessStatSerializer(serializers.ModelSerializer):
   source = serializers.PrimaryKeyRelatedField(many=True, required=False, )
   population = serializers.PrimaryKeyRelatedField(many=True, required=False, )
   subpopulation = serializers.PrimaryKeyRelatedField(many=True, required=False, )
   class Meta:
       model = HomelessStat
       fields = ('id', 'source', 'population', 'subpopulation', 'record_dt', 'record_value')
       depth = 1
