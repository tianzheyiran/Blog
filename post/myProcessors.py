from django.db.models import Count

from post.models import Post


def getPostByCategory(request):

    getPostByCate =Post.objects.values("category__cname","category").annotate(c=Count("*")).order_by("-c")

    from django.db import connection
    cursor = connection.cursor()
    getPostByCreated = cursor.execute("select created,count('*') as count from post_post group by strftime('%Y-%m',created) order by count desc ")

    recentPost = Post.objects.order_by("-created")[:3]

    return {"getPostByCate":getPostByCate,"getPostByCreated":getPostByCreated,"recentPost":recentPost}