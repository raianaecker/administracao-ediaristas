from rest_framework import serializers
from ..models import Usuario

cidade = serializers.SerializerMethodField()

class DiaristasLocalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'reputacao', 'foto_usuario', 'cidade')

    def get_cidade(self, obj):
        return "São Paulo"