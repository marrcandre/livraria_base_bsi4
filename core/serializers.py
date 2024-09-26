from rest_framework.serializers import ModelSerializer

from .models import Categoria, Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
