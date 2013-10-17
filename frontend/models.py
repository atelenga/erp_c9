# encoding: utf-8

# Create your models here.

from django.db import models
from django.forms import ModelForm, extras
from django import forms


class CodeBOM(models.Model):
    code = models.CharField(
        max_length=200, primary_key=True, verbose_name='Код')
    name = models.CharField(max_length=200, verbose_name='Наименование детали')
    cost = models.IntegerField(default=0, verbose_name='Стоимость хранения')

    class Meta:
        verbose_name = 'Код BOM'
        verbose_name_plural = 'Коды BOM'
        ordering = ['code']

    def __unicode__(self):
        return u'%s %s' % (self.code, self.name)


class Supplier(models.Model):
    supplier_name = models.CharField(
        max_length=200, primary_key=True, verbose_name='Поставщик')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    cost = models.IntegerField(default=0, verbose_name='Стоимость доставки')
    time = models.IntegerField(default=0, verbose_name='Время доставки')

    class Meta:
        verbose_name = 'Сведения о поставщике'
        verbose_name_plural = 'Сведения о поставщиках'
        ordering = ['supplier_name']

    def __unicode__(self):
        return u'%s' % (self.supplier_name)


class SupplierProduct(models.Model):
    code = models.ForeignKey(CodeBOM, verbose_name='Код BOM', to_field='code')
    supplier_name = models.ForeignKey(Supplier, verbose_name='Поставщик')
    product_name = models.CharField(
        max_length=200, verbose_name='Наименование продукции')
    cost = models.IntegerField(default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Поставщик и продукция'
        verbose_name_plural = 'Поставщики и продукция'
        ordering = ['code']

    def __unicode__(self):
        return u'%s %s %s' % (self.code, self.product_name, self.supplier_name)


class Remains(models.Model):
    code = models.ForeignKey(CodeBOM, verbose_name='Код BOM')
    name = models.ForeignKey(
        SupplierProduct, verbose_name='Наименование продукции')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    cost = models.IntegerField(default=0, verbose_name='Цена закупки')
    date = models.DateField(max_length=20, verbose_name='Дата закупки')

    class Meta:
        verbose_name = 'Сведения об остатках'
        verbose_name_plural = 'Сведения об остатках'
        ordering = ['code']

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.code, self.name, self.amount, self.cost, self.date)


class Complectation(models.Model):
    code = models.CharField(
        max_length=200, primary_key=True, verbose_name='Код')
    name = models.CharField(max_length=200, verbose_name='Название')
    body_type = models.CharField(max_length=200, verbose_name='Тип кузова')
    body_colour = models.CharField(max_length=200, verbose_name='Цвет кузова')
    engine_volume = models.CharField(
        max_length=200, verbose_name='Объём двигателя')
    transmission = models.CharField(
        max_length=200, verbose_name='Тип трансмиссии')
    fuel_type = models.CharField(max_length=200, verbose_name='Тип горючего')
    tires = models.CharField(max_length=200, verbose_name='Шины')
    wheels = models.CharField(max_length=200, verbose_name='Диски')
    interior = models.CharField(max_length=200, verbose_name='Отделка')

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'
        ordering = ['code']

    def __unicode__(self):
        return u'%s %s ' % (self.code, self.name)


class ProductionPlan(models.Model):
    code = models.CharField(
        max_length=200, primary_key=True, verbose_name='Код заказа')
    complectation = models.ForeignKey(
        Complectation, verbose_name='Комплектация')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    start_date = models.DateField(
        max_length=20, verbose_name='Дата поступления заказа')
    end_date = models.DateField(
        max_length=20, verbose_name='Дата исполнения заказа')

    class Meta:
        verbose_name = 'Производственный план'
        verbose_name_plural = 'Производственные планы'
        ordering = ['code']

    def __unicode__(self):
        return u'%s' % (self.code)


class Order(models.Model):
    code = models.ForeignKey(ProductionPlan, verbose_name='Код заказа')
    name = models.ForeignKey(
        SupplierProduct, verbose_name='Наименование продукции')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    price = models.IntegerField(default=0, verbose_name='Цена закупки')
    date = models.DateField(max_length=20, verbose_name='Дата заказа')

    @property
    def cost(self):
        return self.amount * self.price

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['code']

    def __unicode__(self):
        return u'%s' % (self.code)


class ProcurementPlan(models.Model):
    code = models.ForeignKey(Order, verbose_name='Заказ')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    date = models.DateField(max_length=20, verbose_name='Дата')

    class Meta:
        verbose_name = 'План закупок'
        verbose_name_plural = 'Планы закупок'
        ordering = ['code']

    def __unicode__(self):
        return u'%s %s %s' % (self.code, self.amount, self.date)


class Plan(models.Model):
    code = models.ForeignKey(Order, verbose_name='Код')
    complectation = models.ForeignKey(
        Complectation, verbose_name='Комплектация')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    date = models.DateField(
        max_length=20, verbose_name='Дата', primary_key=True)

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
        ordering = ['code']

    def __unicode__(self):
        return u'%s %s %s %s' % (self.code, self.complectation, self.amount, self.date)


class CodeBOMForm(ModelForm):

    class Meta:
        model = CodeBOM


class RemainsForm(ModelForm):

    class Meta:
        model = Remains


class SupplierForm(ModelForm):

    class Meta:
        model = Supplier


class SupplierProductForm(ModelForm):

    class Meta:
        model = SupplierProduct


class OrderForm(ModelForm):

    class Meta:
        model = Order


class ProcurementPlanForm(ModelForm):

    class Meta:
        model = ProcurementPlan


class ComplectationForm(ModelForm):

    class Meta:
        model = Complectation


class ProductionPlanForm(ModelForm):

    class Meta:
        model = ProductionPlan


class PlanForm(ModelForm):

    class Meta:
        model = Plan