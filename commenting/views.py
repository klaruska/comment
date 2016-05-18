from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.http import Http404
from django.views.generic import TemplateView, ListView, RedirectView
from commenting.models import Post, Comment


class PostView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        posts = Post.objects.all()
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = post
        context['posts'] = posts
        return context


class CommentListView(ListView):
    model = Comment
    template_name = "comment_list.html"
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        post_id = self.kwargs['post_id']
        list_comment = Comment.objects.filter(parent_comment_id__isnull=True, post_id=post_id)
        paginator = Paginator(list_comment, self.paginate_by)
        page = self.request.GET.get('page')
        # result_list = paginator.page(page)

        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator.num_pages)

        if int(page) > int(paginator.num_pages):
            raise Http404

        context['list_coment'] = result_list
        return context


class CommentChildrenListView(ListView):
    model = Comment
    template_name = "comment_list.html"
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super(CommentChildrenListView, self).get_context_data(**kwargs)
        post_id = self.kwargs['post_id']
        comment_id = self.kwargs['comment_id']
        list_comment = Comment.objects.filter(post_id=post_id, parent_comment_id=comment_id)
        paginator = Paginator(list_comment, self.paginate_by)
        page = self.request.GET.get('page')
        # result_list = paginator.page(page)

        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator.num_pages)

        if int(page) > int(paginator.num_pages):
            raise Http404

        context['list_coment'] = result_list
        return context


class CommentLikeView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        comment_id = self.kwargs['comment_id']
        comment = Comment.objects.get(id=comment_id)
        comment.like += 1
        comment.quality += 1
        comment.save()
        # comment.reload()
        return self.request.META['HTTP_REFERER']


class CommentDislikeView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        comment_id = self.kwargs['comment_id']
        comment = Comment.objects.get(id=comment_id)
        comment.dislike += 1
        comment.quality -= 1
        comment.save()
        return self.request.META['HTTP_REFERER']