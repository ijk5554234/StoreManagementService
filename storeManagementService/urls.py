from django.conf.urls import patterns, include, url
import mysite

urlpatterns = patterns('',
                       url(r'^$', 'storeManagementService.views.index'),
                       url(r'^createNewItem/', 'storeManagementService.views.create_new_item'),
                       url(r'^logout/', 'storeManagementService.views.logout'),

                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': mysite.settings.STATICFILES_DIRS, 'show_indexes': True}),
                       )