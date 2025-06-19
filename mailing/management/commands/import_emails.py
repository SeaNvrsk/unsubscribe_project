from django.core.management.base import BaseCommand
from mailing.models import Subscriber

class Command(BaseCommand):
    help = 'Импорт email-адресов из файла'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к файлу с email-адресами')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        created = 0
        with open(file_path, 'r') as file:
            for line in file:
                email = line.strip()
                if email:
                    obj, was_created = Subscriber.objects.get_or_create(email=email)
                    if was_created:
                        created += 1
        self.stdout.write(self.style.SUCCESS(f'Импортировано {created} email-адресов.'))
