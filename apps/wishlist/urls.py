from django.conf.urls import url
from . import views   






       
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^dashboard$',views.dashboard),
    url(r'^addwish$',views.addwish),
    url(r'^add_wish$',views.add_wish),
    url(r'^deletewish/(?P<wish_id>\d+)$',views.deletewish),
    url(r'^removewish/(?P<wish_id>\d+)$',views.removewish),
    url(r'^joinwish/(?P<wish_id>\d+)$',views.joinwish),
    url(r'^desire/(?P<item_id>\d+)$',views.desire)
    # put in view
  ]
