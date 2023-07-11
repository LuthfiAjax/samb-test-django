from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('penerimaan-barang/', views.penerimaan_barang,
         name='penerimaan_barang'),
    path('pengeluaran-barang/', views.pengeluaran_barang,
         name='pengeluaran_barang'),
]
