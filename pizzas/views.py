from .serializer import PizzasSerializer
from .models import Pizzas
from rest_framework import viewsets

class PizzasView(viewsets.ModelViewSet):
    serializer_class=PizzasSerializer
    queryset=Pizzas.objects.all()