from rest_framework import serializers
from .models import Pizzas

class PizzasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pizzas
        fields='__all__'