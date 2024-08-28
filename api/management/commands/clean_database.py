from django.core.management.base import BaseCommand
from ...models import Task  # Importuj model do wyczyszczenia

class Command(BaseCommand):
    help = 'Czyści bazę danych'

    def handle(self, *args, **kwargs):
        Task.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Baza danych została wyczyszczona.'))