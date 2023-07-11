from django.db import models

class Supplier(models.Model):
    SupplierPK = models.IntegerField(primary_key=True)
    SupplierName = models.CharField(max_length=255)

class Customer(models.Model):
    CustomerPK = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=255)

class Product(models.Model):
    ProductPK = models.IntegerField(primary_key=True)
    ProductName = models.CharField(max_length=255)

class Warehouse(models.Model):
    WhsPK = models.IntegerField(primary_key=True)
    WhsName = models.CharField(max_length=255)

class PenerimaanBarangHeader(models.Model):
    TrxInPK = models.AutoField(primary_key=True)
    TrxInNo = models.CharField(max_length=255)
    WhsIdf = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    TrxInDate = models.DateField()
    TrxInSuppIdf = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    TrxInNotes = models.CharField(max_length=255)

class PenerimaanBarangDetail(models.Model):
    TrxInDPK = models.AutoField(primary_key=True)
    TrxInIDF = models.ForeignKey(PenerimaanBarangHeader, on_delete=models.CASCADE)
    TrxInDProductIdf = models.ForeignKey(Product, on_delete=models.CASCADE)
    TrxInDQtyDus = models.IntegerField()
    TrxInDQtyPcs = models.IntegerField()

class PengeluaranBarangHeader(models.Model):
    TrxOutPK = models.AutoField(primary_key=True)
    TrxOutNo = models.CharField(max_length=255)
    WhsIdf = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    TrxOutDate = models.DateField()
    TrxOutSuppIdf = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    TrxOutNotes = models.CharField(max_length=255)

class PengeluaranBarangDetail(models.Model):
    TrxOutDPK = models.AutoField(primary_key=True)
    TrxOutIDF = models.ForeignKey(PengeluaranBarangHeader, on_delete=models.CASCADE)
    TrxOutDProductIdf = models.ForeignKey(Product, on_delete=models.CASCADE)
    TrxOutDQtyDus = models.IntegerField()
    TrxOutDQtyPcs = models.IntegerField()
