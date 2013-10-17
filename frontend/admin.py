# encoding: utf-8

from django.contrib import admin
from frontend.models import CodeBOM, Remains, Supplier, SupplierProduct, Order, ProcurementPlan, Complectation, ProductionPlan, Plan

admin.site.register(CodeBOM)
admin.site.register(Remains)
admin.site.register(Supplier)
admin.site.register(SupplierProduct)
admin.site.register(Order)
admin.site.register(ProcurementPlan)
admin.site.register(Complectation)
admin.site.register(ProductionPlan)
admin.site.register(Plan)
