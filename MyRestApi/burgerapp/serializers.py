from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import UserProfile, Order, Ingredient, CustomerDetails


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password')

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient

        exclude = ["id", ]


class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomerDetails

        exclude = ["id", ]


class OrderSerializer(ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerDetailSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        ingredientData = validated_data.pop("ingredients")
        customerData = validated_data.pop("customer")
        ingredients = IngredientSerializer.create(
            IngredientSerializer(), validated_data=ingredientData)
        customer = CustomerDetailSerializer.create(
            CustomerDetailSerializer(), validated_data=customerData)
        order, created = Order.objects.update_or_create(
            ingredients=ingredients,
            customer=customer,
            price=validated_data.pop("price"),
            orderTime=validated_data.pop("orderTime"),
            user=validated_data.pop("user")
        )

        return order
