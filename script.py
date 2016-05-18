from django.utils import timezone
from random import randint
from django.utils.lorem_ipsum import words, sentence, paragraphs
from commenting.models import Post, Comment


def commenting(diving, post, parent_comment, n):
    for child_comment in range(n):
        author = words(2, common=True)
        content = sentence()
        like = randint(0, 150)
        dislike = randint(0, 50)
        quality = like - dislike
        create_date = post.create_date
        parent = parent_comment
        new_comment = Comment(author=author, content=content, like=like, dislike=dislike, quality=quality,
                              create_date=create_date, post=post, parent_comment=parent)
        new_comment.save()
        if new_comment.parent_comment:
            parent_comment_id = new_comment.parent_comment.id
        else:
            parent_comment_id = None
        print("Post: %s, parent comment: %s, comment: %s" %
              (post.id, parent_comment_id, new_comment.id))
        if diving > 0:
            commenting(diving - 1, post, new_comment, n - 6)


def posting():

    now = timezone.now()
    for i in range(3):
        post_author = words(2, common=True)
        post_title = words(4, common=True)
        post_content = paragraphs(4, common=True)
        post_create_date = now
        new_post = Post(author=post_author, title=post_title, content=post_content, create_date=post_create_date)
        new_post.save()
        commenting(3, new_post, None, 19)


posting()