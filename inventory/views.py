from django.shortcuts import render
from .models import PenerimaanBarangHeader, PenerimaanBarangDetail, PengeluaranBarangHeader, PengeluaranBarangDetail


def penerimaan_barang(request):
    if request.method == 'POST':
        # Proses form penerimaan barang
        pass
    else:
        # Tampilkan form penerimaan barang
        return render(request, 'inventory/penerimaan_barang.html')


def pengeluaran_barang(request):
    if request.method == 'POST':
        # Proses form pengeluaran barang
        pass
    else:
        # Tampilkan form pengeluaran barang
        return render(request, 'inventory/pengeluaran_barang.html')
