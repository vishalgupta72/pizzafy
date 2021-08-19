from rest_framework import serializers, viewsets, routers
from .models import Pizza


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ('type', 'size', 'toppings')


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


router = routers.DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
