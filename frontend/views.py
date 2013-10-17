# encoding: utf-8

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from frontend.models import *
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from django.template import RequestContext


def index(request):
    productionplans = ProductionPlan.objects.all()
    return render_to_response(
        "index.html", {"productionplans": productionplans},
        context_instance=RequestContext(request))


def codebom(request):
    form = CodeBOMForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("codebom.html", {"form": form},
                              context_instance=RequestContext(request))


def remains(request):
    form = RemainsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("remains.html", {"form": form},
                              context_instance=RequestContext(request))


def orders(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("orders.html", {"form": form},
                              context_instance=RequestContext(request))


def complectations(request):
    form = ComplectationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("complectations.html", {"form": form},
                              context_instance=RequestContext(request))


def supplier(request):
    form = SupplierForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("supplier.html", {"form": form},
                              context_instance=RequestContext(request))


def supplierproduct(request):
    form = SupplierProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("supplierproduct.html", {"form": form},
                              context_instance=RequestContext(request))


def productionplan(request):
    form = ProductionPlanForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')

    return render_to_response("productionplan.html", {"form": form},
                              context_instance=RequestContext(request))


def supplierlist(request):
    suppliers = Supplier.objects.all()
    return render_to_response("supplierlist.html", {"suppliers": suppliers},
                              context_instance=RequestContext(request))


def remainslist(request):
    remains = Remains.objects.all()
    return render_to_response("remainslist.html", {"remains": remains},
                              context_instance=RequestContext(request))


def diagrambom(request):
    codes = CodeBOM.objects.all()
    return render_to_response("diagrambom.html", {"codes": codes},
                              context_instance=RequestContext(request))


def supplierproductlist(request):
    supplierproducts = SupplierProduct.objects.all()
    return render_to_response(
        "supplierproductlist.html", {"supplierproducts": supplierproducts},
        context_instance=RequestContext(request))


def complectationslist(request):
    complectations = Complectation.objects.all()
    return render_to_response(
        "complectationslist.html", {"complectations": complectations},
        context_instance=RequestContext(request))


def productionplanlist(request):
    productionplans = ProductionPlan.objects.all()
    return render_to_response(
        "productionplanlist.html", {"productionplans": productionplans},
        context_instance=RequestContext(request))


def orderslist(request):
    orders = Order.objects.all()
    return render_to_response("orderslist.html", {"orders": orders},
                              context_instance=RequestContext(request))


def selectproduct(request, rec_id):
    try:
        res_id = int(rec_id)
    except ValueError:
        raise Http404()

    productionplan = ProductionPlan.objects.get(code=rec_id)
    remains_lifo = Remains.objects.filter(date__lte=productionplan.end_date)
    remains_fifo = Remains.objects.filter(date__gte=productionplan.start_date)
    remains_avg = Remains.objects.all()

    r_lifo = r_fifo = r_average = 0
    for remain_lifo in remains_lifo:
        r_lifo += remain_lifo.cost * remain_lifo.amount

    for remain_fifo in remains_fifo:
        r_fifo += remain_fifo.cost * remain_fifo.amount

    i = 0
    for remain_avg in remains_avg:
        i += 1
        r_average = (remain_avg.cost * remain_avg.amount) / i

    orders_q = Order.objects.filter(code=rec_id)
    orders_lifo = orders_q.filter(date__lte=productionplan.end_date)
    orders_fifo = orders_q.filter(date__gte=productionplan.start_date)
    orders_avg = orders_q.all()

    o_lifo = o_fifo = o_average = 0
    for order_lifo in orders_lifo:
        o_lifo += order_lifo.cost * order_lifo.amount

    for order_fifo in orders_fifo:
        o_fifo += order_fifo.cost * order_fifo.amount

    i = 0
    for order_avg in orders_avg:
        i += 1
        o_average = (order_avg.cost * order_avg.amount) / i

    if (o_lifo == 0) and (o_fifo == 0) and (o_average == 0):
    	o_fifo = o_lifo = o_average = "Нет заказов деталей для выбранного плана производства"

    return render_to_response(
        "resultproduct.html", {
            "r_lifo": r_lifo, "r_fifo": r_fifo, "r_average": r_average,
            "o_lifo": o_lifo, "o_fifo": o_fifo, "o_average": o_average,
            "productionplan": productionplan, },
        context_instance=RequestContext(request))