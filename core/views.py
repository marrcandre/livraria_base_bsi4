from rest_framework.viewsets import ModelViewSet

from .models import Categoria, Livro
from .serializers import CategoriaSerializer, LivroSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.order_by('titulo')
    serializer_class = LivroSerializer
