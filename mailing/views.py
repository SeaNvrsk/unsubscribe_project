from django.shortcuts import render
from .models import Subscriber
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Subscriber
import openpyxl
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv
from .models import Subscriber
import uuid


def unsubscribe_view(request):
    token = request.GET.get("token")
    if token:
        try:
            subscriber = Subscriber.objects.get(unsubscribe_token=token)
            subscriber.is_unsubscribed = True
            subscriber.save()
            return render(request, "mailing/success.html", {"email": subscriber.email})
        except Subscriber.DoesNotExist:
            return render(request, "mailing/invalid.html")
    else:
        return render(request, "mailing/invalid.html")

@login_required
def upload_excel(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["file"]
            wb = openpyxl.load_workbook(excel_file)
            ws = wb.active

            count = 0
            for row in ws.iter_rows(min_row=2, values_only=True):
                email = row[0]
                if email:
                    _, created = Subscriber.objects.get_or_create(email=email)
                    if created:
                        count += 1
            return render(request, "mailing/upload_success.html", {"count": count})
    else:
        form = UploadFileForm()
    return render(request, "mailing/upload.html", {"form": form})


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subscribers.csv"'

    writer = csv.writer(response)
    writer.writerow(['email', 'unsubscribe_url'])

    for sub in Subscriber.objects.filter(is_unsubscribed=False):
        unsubscribe_url = f"https://unsubscribe.recovia.solutions/unsubscribe/?token={sub.unsubscribe_token}"
        writer.writerow([sub.email, unsubscribe_url])

    return response

def index(request):
    form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def upload_subscribers(request):
    if request.method == 'POST' and request.FILES['file']:
        wb = openpyxl.load_workbook(request.FILES['file'])
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            email = row[0]
            if email:
                Subscriber.objects.get_or_create(
                    email=email,
                    defaults={'unsubscribe_token': uuid.uuid4()})
    return redirect('index')

def export_subscribers(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Email', 'Dado de baja', 'Token'])

    for s in Subscriber.objects.all():
        ws.append([s.email, 'Sí' if s.is_unsubscribed else 'No', str(s.unsubscribe_token)])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=subscribers.xlsx'
    wb.save(response)
    return response