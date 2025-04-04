from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# ListView to display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# DetailView for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView for new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView to edit posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form)