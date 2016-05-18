from django.conf.urls import include, url
from django.contrib import admin
from commenting.views import PostView, CommentListView, CommentLikeView, CommentDislikeView, CommentChildrenListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<post_id>\d+)/$', PostView.as_view(), name='post'),
    url(r'^comment/(?P<comment_id>\d+)/like/$', CommentLikeView.as_view(), name='comment_like'),
    url(r'^comment/(?P<comment_id>\d+)/dislike/$', CommentDislikeView.as_view(), name='comment_dislike'),
    url(r'^post/(?P<post_id>\d+)/comment_list/?$', CommentListView.as_view(), name='comment_list'),
    url(r'^post/(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/comment_list/?$', CommentChildrenListView.as_view(), name='comment_children_list'),
]
