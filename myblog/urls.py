from django.conf.urls import url
from myblog.views import list_view, detail_view, post_new


urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),
    url(r'^post/new/$',
        post_new,
        name='post_new'),
]
