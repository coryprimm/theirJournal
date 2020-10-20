from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^indexTwo$', views.indexTwo),
    url(r'^add_item$', views.add_item),
    url(r'^mainEntList$', views.mainList),
    url(r'^add_tagz_base$', views.add_tagz_base),
]