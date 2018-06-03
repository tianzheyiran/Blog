# coding = utf-8

from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$',views.index_view,name="homepage"),
    url(r"^post/(\d+)",views.detials_view),
    url(r"^page/(\d+)",views.index_view),
    url(r"^category/(\d+)",views.indexByCategory_view),
    url(r"^archive/(\d+)/(\d+)",views.indexByDate_view),
    url(r"^archive/",views.postall,name="postall"),
    url(r'^search/$',views.search_view),
]