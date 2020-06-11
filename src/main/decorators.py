from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Exists
from django.shortcuts import redirect
from main.models import Post

class PostTest(UserPassesTestMixin):
    def test_func(self):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        return post.author == self.request.user
    def handle_no_permission(self):
        return redirect('post-details', pk=self.kwargs['pk'])