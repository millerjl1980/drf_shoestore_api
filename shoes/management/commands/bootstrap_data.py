from django.core.management.base import BaseCommand
from shoes.models import ShoeType, ShoeColor

# https://labofcoding.com/custom-django-management-commands/
class Command(BaseCommand):
    help = 'Loads base data for shoe types and color'

    def handle(self, *args, **options):
        s_types = ['sneaker', 'boot', 'sandal', 'dress', 'other']

        for s_type in s_types:
            new_type = ShoeType.objects.create(style=s_type)
            new_type.save()
        
        s_colors = [
            ShoeColor.red,
            ShoeColor.orange,
            ShoeColor.yellow, 
            ShoeColor.green,
            ShoeColor.blue,
            ShoeColor.indego,
            ShoeColor.violet,
            ShoeColor.black,
            ShoeColor.white
        ]

        for s_color in s_colors:
            new_color = ShoeColor.objects.create(color_name=s_color)
            new_color.save()
     
        self.stdout.write(self.style.SUCCESS('Shoe types and colors created successfully.'))