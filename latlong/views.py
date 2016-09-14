from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import csv
from csv_handler import *


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('./media/output.csv', 'w') as output_file:
                geocode_uploaded_file(request.FILES['file'], output_file)
            with open('./media/output.csv', 'rb') as download_file:
                response = HttpResponse(download_file.read(), content_type="text/csv")
                response['Content-Disposition'] = 'inline; filename=output.csv'
                return response
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
