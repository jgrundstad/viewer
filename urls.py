from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

import views
import update_views


urlpatterns = patterns('',
                       # Access pages
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^restricted/$', views.restricted,
                           name='restricted'),
                       url(r'^permission/$', views.permission,
                           name='permission'),
                       # Bnid
                       url(r'^new_bionimbus_id/$',
                           views.new_bionimbus_id, name='new_bionimbus_id'),
                       url(r'^get_bnids_by_study/(?P<study_id>\d+)/$',
                           views.get_bnids_by_study, name='get_bnids_by_study'),
                       url(r'bnid_edit/(?P<bnid_id>\d+)/$',
                           views.edit_bionimbus_id, name='bnid_edit'),
                       # Sample
                       url(r'^new_sample/$', views.new_sample,
                           name='new_sample'),
                       url(r'^get_samples/(?P<study_id>\d+)/$', views.get_samples,
                           name='get_samples'),
                       url(r'sample_edit/(?P<sample_id>\d+)/$',
                           views.edit_sample, name='sample_edit'),
                       # Study
                       url(r'^new_study/$', views.new_study, name='new_study'),
                       url(r'study_edit/(?P<study_id>\d+)/$',
                           views.edit_study, name='study_edit'),
                       # Report
                       url(r'^upload_report/$', views.upload_report,
                           name='upload_report'),
                       url(r'^load_variants/(?P<report_id>\d+)/$', views.load_variants,
                           name='load_variants'),
                       url(r'^files/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'view_report/(?P<file_id>\d+)/$',
                           views.view_report, name='view_report'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)