from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')

class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style', )

class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color_name', )

class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'size',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        )