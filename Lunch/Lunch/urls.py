
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/','lunchSelector.views.show_index',name='show_index'),
    url(r'^submit/','lunchSelector.views.submit',name='submit'),
    url(r'^results/','lunchSelector.views.show_results',name='show_results'),
    url(r'^reset/','lunchSelector.views.reset',name='reset'),
    url(r'^view/','lunchSelector.views.view_count',name='view_count'),
    url(r'^save/','lunchSelector.views.save_data',name='save_data'),
    url(r'^menuChooser/','lunchSelector.views.menu_chooser',name='menu_chooser'),
]
