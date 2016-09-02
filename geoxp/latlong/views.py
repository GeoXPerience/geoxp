from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #this method will be implemented later
            #handle_uploaded_file(request.FILES[''])
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
