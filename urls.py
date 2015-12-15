from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import views

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
                       url(r'^users/change-password/', 'django.contrib.auth.views.password_change',
                           {
                               'template_name': 'viewer/change_password.html',
                               'post_change_redirect': '/viewer/users/change-password-done/',
                           }, name='change-password'),
                       url(r'^users/change-password-done/', 'django.contrib.auth.views.password_change_done',
                           {
                               'template_name': 'viewer/change_password_done.html'
                           }, name='change-password-done'),

                       url(r'^populate-sidebar/$', views.populate_sidebar, name='populate_sidebar'),

                       # Errors
                       url(r'^error/no_project/$', views.no_project, name='no_project'),
                       url(r'^error/not-found/$', lambda request: render(request, 'viewer/error/404_error.html')),

                       # Project
                       url(r'^project/$', views.manage_project,
                           name='manage_project'),
                       url(r'^project/new_project/$',
                           views.new_project, name='new_project'),
                       url(r'^project/edit_project/(?P<project_id>\d+)/$',
                           views.edit_project, name='edit_project'),
                       url(r'^get_all_projects/$', views.get_all_projects,
                           name='get_all_projects'),


                       # Bnid
                       url(r'^bnid/$',
                           views.manage_bnid, name='manage_bnid'),
                       url(r'^bnid/(?P<set_viewing_project_pk>\d+)/$', views.manage_bnid,
                           name='manage_bnid_set_viewing_project_pk'),
                       url(r'^bnid/new_bnid/$',
                           views.new_bnid, name='new_bnid'),
                       url(r'^bnid/edit_bnid/(?P<bnid_id>\d+)/$',
                           views.edit_bnid, name='edit_bnid'),
                       url(r'^bnid/delete_bnid/(?P<bnid_id>\d+)/$',
                           views.delete_bnid, name='delete_bnid'),
                       url(r'^get_bnids_by_study/(?P<study_id>\d+)/$',
                           views.get_bnids_by_study, name='get_bnids_by_study'),


                       # Sample
                       url(r'^sample/$', views.manage_sample,
                           name='manage_sample'),
                       url(r'^sample/(?P<set_viewing_project_pk>\d+)/$', views.manage_sample,
                           name='manage_sample_set_viewing_project_pk'),
                       url(r'^sample/new_sample/$', views.new_sample,
                           name='new_sample'),
                       url(r'edit_sample/(?P<sample_id>\d+)/$', views.edit_sample,
                           name='edit_sample'),
                       url(r'delete_sample/(?P<sample_id>\d+)/$', views.delete_sample,
                           name='delete_sample'),
                       url(r'^get_samples/(?P<study_id>\d+)/$', views.get_samples,
                           name='get_samples'),

                       # Study
                       url(r'^study/$', views.manage_study, name='manage_study'),
                       url(r'^study/(?P<set_viewing_project_pk>\d+)$', views.manage_study,
                           name='manage_study_set_viewing_project_pk'),
                       url(r'^study/new_study/$', views.new_study, name='new_study'),
                       url(r'^study/edit_study/(?P<study_id>\d+)/$',
                           views.edit_study, name='edit_study'),
                       url(r'^study/delete_study/(?P<study_id>\d+)/$',
                           views.delete_study, name='delete_study'),

                       # Report
                       url(r'^report/$', views.manage_report,
                           name='manage_report'),
                       url(r'^report/(?P<set_viewing_project_pk>\d+)/$', views.manage_report,
                           name='manage_report_set_viewing_project_pk'),
                       url(r'^report/edit_report/(?P<report_id>\d+)/$',
                           views.edit_report, name='edit_report'),
                       url(r'report/view_report/(?P<file_id>\d+)/$',
                           views.view_report, name='view_report'),
                       url(r'^report/upload_report/$', views.upload_report,
                           name='upload_report'),
                       url(r'^report/delete_report/(?P<report_id>\d+)/$', views.delete_report,
                           name='delete_report'),
                       url(r'^load_variants/(?P<report_id>\d+)/$', views.load_variants,
                           name='load_variants'),
                       url(r'^report/zip-and-download/', views.zip_and_download, name='zip_and_download'),

                       # Share
                       url(r'^shared/view/(?P<shared_data_uuid>[\da-f\-]+)/$', views.view_shared_data,
                           name='view_shared_data'),
                       url(r'^shared/share_report/$', views.share_report, name='share_report_post'),
                       # url(r'^shared/share_report/(?P<report_id>\d+)/$', views.share_report, name='share_report'),
                       url(r'^error/share_data_expired/$',
                           views.view_share_data_expired, name='view_shared_data_expired'),
                       url(r'^error/share_data_dne/$', views.view_share_data_dne, name='share_report'),

                       url(r'^files/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),

                       # Contact
                       url(r'^contact/$', views.manage_contact,
                           name='manage_contact'),
                       url(r'^contact/(?P<set_viewing_project_pk>\d+)/$', views.manage_contact,
                           name='manage_contact_set_viewing_project_pk'),
                       url(r'^contact/new_contact/$', views.new_contact,
                           name='new_contact'),
                       url(r'^contact/new_contact_from_share/$', views.new_contact_from_share,
                           name='new_contact'),
                       url(r'^contact/edit_contact/(?P<contact_id>\d+)/$', views.edit_contact,
                           name='edit_contact'),
                       url(r'^contact/delete_contact/(?P<contact_id>\d+)/$', views.delete_contact,
                           name='delete_contact'),
                       url(r'^contact/get_contacts_json/(?P<project_id>\d+)/$', views.get_contacts_json,
                           name='get_contacts'),

                       # Search
                       url(r'^search/$', views.search_reports, name='search_reports'),
                       url(r'^search/(?P<set_viewing_project_pk>\d+)/$', views.search_reports,
                           name='search_reports_set_viewing_project_pk'),
                       url(r'^ajax_search_reports/(?P<search_col>\S+)/(?P<search_term>\S+)/(?P<search_type>\S+)/$',
                           views.ajax_search_reports, name='ajax_search_reports'),
                       url(r'^ajax_search_reports/(?P<search_col>\S+)/(?P<search_term>\S+)/(?P<search_type>\S+)/(?P<reports_ids>\S+)/$',
                           views.ajax_search_reports, name='ajax_search_reports'),


                       # Info
                       url(r'^info/$', views.info_many, name='info_many'),
                       url(r'^info/(?P<report_id>\d+)/$', views.info, name='info'),
                       url(r'^cards/get/$', views.get_cards, name='get_cards'),
                       # url(r'^cards/gene/(?P<report_id>\d+)/$', views.cards, name='cards_report'),
                       url(r'^get_series_data/$', views.get_series_data, name='get_series_data')

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


