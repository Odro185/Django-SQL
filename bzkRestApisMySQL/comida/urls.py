from django.conf.urls import url 
from comida import views 
 
urlpatterns = [ 
    url(r'^api/comida$', views.tutorial_list),
    url(r'^api/comida/(?P<pk>[0-9]+)$', views.comida_detail),
    url(r'^api/comida/published$', views.comida_list_published)
]
