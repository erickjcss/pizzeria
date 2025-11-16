from .serializer import ComentariosSerializer
from .models import Comentarios
from rest_framework import viewsets

class ComentariosView(viewsets.ModelViewSet):
    serializer_class=ComentariosSerializer
    queryset=Comentarios.objects.all()