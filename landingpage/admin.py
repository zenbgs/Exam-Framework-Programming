from django.contrib import admin

# Register your models here.
from .models import Barang
from .models import Transaksi
from .models import Detailtrans
from .models import Jenis

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_Field=['kodebrg','nama']
    list_filter=['jenis_id']
    list_per_page=5




admin.site.register(Transaksi,list_display=('kodetrans','tgltrans','total'))
admin.site.register(Detailtrans,list_display=('kodetrans','kodebrg','qty','subtotal'))
admin.site.register(Jenis,list_display=('nama','ket'))
admin.site.register(Barang,kolomBarang)
