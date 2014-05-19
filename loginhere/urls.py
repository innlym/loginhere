from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'index.views.index', name='index'),
    url(r'^about/$', 'index.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api/', include('api.urls')),
)

# if settings.DEBUG == True:
#     urlpatterns += patterns('',
#         url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
#     )
