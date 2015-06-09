from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

import views
import update_views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^restricted/$', views.restricted,
                           name='restricted'),
                       url(r'^permission/$', views.permission,
                           name='permission'),

                       url(r'^new_bionimbus_id/$',
                           views.new_bionimbus_id, name='new_bionimbus_id'),
                       #url(r'^new_bionimbus_id/(?P<study_id>\d+)/$',
                       #    views.new_bionimbus_id, name='new_study_bionimbus_id'),

                       url(r'^new_sample/$', views.new_sample,
                           name='new_sample'),
                       url(r'^get_samples/(?P<study_id>\d+)/$', views.get_samples,
                           name='get_samples'),
                       url(r'^new_study/$', views.new_study, name='new_study'),
                       url(r'^upload_report/$', views.upload_report,
                           name='upload_report'),
                       url(r'^files/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'view_report/(?P<file_id>\d+)/$',
                           views.view_report, name='view_report'),
                       url(r'study_edit/(?P<study_id>\d+)/$',
                           views.edit_study, name='study_edit'),
                       url(r'sample_edit/(?P<sample_id>\d+)/$',
                           views.edit_sample, name='sample_edit'),
                       url(r'bnid_edit/(?P<bnid_id>\d+)/$',
                           views.edit_bionimbus_id, name='bnid_edit'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)