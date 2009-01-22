from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import pages.urls

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^blog/', include('microblog.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    import os.path
    args = []
    for k, path in settings.STATIC_DIRS.items():
        args.append((
            r'^static/%s/(?P<path>.*)$' % k,
            'django.views.static.serve',
            {'document_root': os.path.join(path, k), 'show_indexes': True}
        ))
    urlpatterns += patterns('', *args)

urlpatterns = urlpatterns + pages.urls.urlpatterns
