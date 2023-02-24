from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import *
class table_serializer(DocumentSerializer):
    class Meta:
        model=table_list
        fields="__all__"
class user_serializer(DocumentSerializer):
    class Meta:
        model=user
        fields="__all__"