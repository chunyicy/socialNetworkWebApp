from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    View
)
from .models import Post
from .models import Friend

from users.models import Profile
from django.urls import reverse

from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    template_name = 'social/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('social-home')



def UserSearch(request):
    if request.method == "POST":
        searched = request.POST['searched']
        profile_list=Profile.objects.filter(user__username__icontains=searched) 
        context ={
            'searched':searched,
            'profile_list':profile_list
        }
        return render(request, 'social/search.html',context)
    else:
        return render(request, 'social/search.html',{})



def listusers(request):
    posts = Post.objects.all().order_by()
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.filter(current_user=request.user).first()
    if friend:
        friends = friend.users.all()
    else: 
        friends = User.objects.none()


    context = {
        'posts': posts, 'users': users, 'friends': friends
    }
    return render(request, 'social/list_users.html', context)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('listusers')


class ProfileView(View):

    def get(self, request, pk,*args, **kwargs):
        # profile=Profile.objects.get(pk=pk)
        user=User.objects.get(pk=pk)
        posts=Post.objects.filter(author=user).order_by('-date_posted')




        context={
            'user':user,
            # 'profile':profile,
            'posts':posts,
          
        }
        return render(request, 'social/user_profile.html',context)