from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render
from landingpage.models import Barang,Tanaman,JenisTanaman
from landingpage.forms import TanamanForm

#Create your views here



def barang_view(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs': barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def tanaman(request):
    if request.POST:
        kodetanaman=request.POST['kodetanaman']
        nama=request.POST['nama']
        stok=request.POST['stok']
        harga=request.POST['harga']
        link=request.POST['link']
        query=Tanaman.objects.create(kodetanaman=kodetanaman, nama=nama, stok=stok, harga=harga, link=link)
        query.save()
        messages.success(request, "Berhasil Tambah Data")
        
        konteks={
            'tanaman': Tanaman.objects.all(),
        }

        return render(request, 'uts/index.html', konteks)

    else:
        tanaman=Tanaman.objects.all()

        konteks={
            'tanaman': tanaman,
        }

        return render(request,'uts/index.html',konteks)

def edit_tanaman(request, id):
    object = Tanaman.objects.get(id=id)
    form = TanamanForm(request.POST, instance=object)
    if form.is_valid():
        form.save()
        messages.success(request, "Berhasil Edit Data")
    
    konteks={
            'tanaman': Tanaman.objects.all(),
    }
    return render(request, 'uts/index.html', konteks)

def jenis_tanaman(request):
    jenis_tanaman=JenisTanaman.objects.all()

    konteks={
        'jenis_tanaman': jenis_tanaman,
    }

    return render(request,'uts/jenis_tanaman.html',konteks)