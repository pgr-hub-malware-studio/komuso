from django.conf.urls import patterns, include, url

urlpatterns = patterns('score-editor.views',
    url(r'^$', 'home'),
    url(r'^export-pdf/', 'home_pdf'),
)
