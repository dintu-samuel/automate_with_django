
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Greet the user"



    def add_arguments(self, parser):
        parser.add_argument('name',type=str, help="Specifies the username")
    

    def handle(self, *args, **kwargs): 
        name = kwargs['name']
        greeting = f'Hi {name}, good morning'
        self.stdout.write(self.style.SUCCESS(greeting))