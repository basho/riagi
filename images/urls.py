from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('images.views',
    url(r'^$', 'index', name='index'),
)
