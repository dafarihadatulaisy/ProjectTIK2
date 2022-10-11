from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodi6(request):
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip/index.html', konteks)

