from django.core.management.base import BaseCommand
from shoes.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Loads base data for shoe types and color'

    def handle(self, *args, **options):
        s_types = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        type_data = []
        for s_type in s_types:
            new_type = ShoeType.objects.create(style=s_type)
            new_type.save()
            
     
        self.stdout.write(self.style.SUCCESS('Shoe types and colors created successfully.'))

           # s_colors = [
        #     models.red,
        #     models.orange,
        #     models.yellow, 
        #     models.green,
        #     models.blue,
        #     models.indego,
        #     models.violet,
        #     models.black,
        #     models.white
        # ]
        # ShoeColor.objects.bulk_create(s_colors)