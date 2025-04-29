from django.core.management.base import BaseCommand
from mailing.models import Subscriber
import openpyxl


class Command(BaseCommand):
    help = "Импорт подписчиков из Excel"

    def handle(self, *args, **kwargs):
        wb = openpyxl.load_workbook('subscribers.xlsx')
        ws = wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):
            email = row[0]
            if email:
                Subscriber.objects.get_or_create(email=email)

        self.stdout.write(self.style.SUCCESS("Импорт завершён."))