from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount' # rendering the get_discount model method with other name
        ]
    
    def get_my_discount(self, obj):
        """
        Getting get_discount Model method
        """
        return obj.get_discount()