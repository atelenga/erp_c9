from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from frontend import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'erp.views.home', name='home'),
                       # url(r'^frontend/', include('frontend.urls')),
                       url(r'^$', views.index, name='index'),
                       url(r'^codebom/', views.codebom, name='codebom'),
                       url(r'^remains/', views.remains, name='remains'),
                       url(r'^supplier/', views.supplier, name='supplier'),
                       url(r'^productionplan/',
                           views.productionplan, name='productionplan'),
                       url(r'^orders/', views.orders, name='orders'),
                       url(r'^complectations/',
                           views.complectations, name='complectations'),
                       url(r'^supplierlist/',
                           views.supplierlist, name='supplierlist'),
                       url(r'^supplierproduct/',
                           views.supplierproduct, name='supplierproduct'),
                       url(r'^remainslist/',
                           views.remainslist, name='remainslist'),
                       url(r'^diagrambom/',
                           views.diagrambom, name='diagrambom'),
                       url(r'^supplierproductlist/',
                           views.supplierproductlist, name='supplierproductlist'),
                       url(r'^complectationslist/',
                           views.complectationslist, name='complectationslist'),
                       url(r'^productionplanlist/',
                           views.productionplanlist, name='productionplanlist'),
                       url(r'^orderslist/',
                           views.orderslist, name='orderslist'),                       
                       url(r'^selectproduct/(?P<rec_id>\d+)/$',
                           views.selectproduct, name='selectproduct'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       ) 