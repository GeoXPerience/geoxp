from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import csv
from csv_handler import *


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('./media/output.csv', 'a') as output_file:
                geocode_uploaded_file(request.FILES['file'], output_file)
            return HttpResponse("Sucesso")
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
