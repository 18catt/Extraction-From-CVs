from django.shortcuts import render, redirect
from .forms import CVUploadForm
from .utils import process_cvs

#Create your views here
def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('download')
    else:
        form = CVUploadForm()
    return render(request, 'upload.html', {'form': form})

def download(request):
    process_cvs('Sample2')
    return render(request, 'download.html')

