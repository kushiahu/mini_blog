from django.forms.models import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
	CreateView, ListView, UpdateView,
	DeleteView, DetailView
)

from posts.models import Post

from posts.forms import PostFormModel


# def home(request):
# 	posts = Post.objects.all()
# 	return render(request, 'posts/all.html', {'posts': posts})


class HomeView(ListView):
	context_object_name = 'posts'
	model = Post
	ordering = ['-id']
	template_name = 'posts/all.html'


# def add_view(request):
# 	form = PostFormModel(request.POST, request.FILES or None)
# 	if request.method == 'POST' and form.is_valid():
# 		form.save()
# 		return redirect('dashboard')
# 	return render(request, 'posts/create.html', {'form': form})


class AddPostView(CreateView):
	form_class = PostFormModel
	model = Post
	template_name = 'posts/create.html'
	success_url = reverse_lazy('dashboard')


def dashboard_view(request):
	posts = Post.objects.all().order_by('-id')
	return render(request, 'posts/dash.html', {'posts': posts})


# def update_view(request, id):
# 	post = get_object_or_404(Post, pk=id)

# 	if request.method == 'POST':
# 		form = PostFormModel(request.POST, request.FILES, instance=post)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('dashboard')
# 	else:
# 		form = PostFormModel(instance=post)
# 	return render(request, 'posts/update.html', {'form': form})


class UpdatePostView(UpdateView):
	form_class = PostFormModel
	model = Post
	template_name = 'posts/update.html'
	success_url = reverse_lazy('dashboard')
	pk_url_kwarg = 'id'


# def delete_view(request, id):
# 	post = get_object_or_404(Post, pk=id)
# 	if request.method == 'POST':
# 		post.delete()
# 		return redirect('dashboard')
# 	return render(request, 'posts/delete.html', {'post': post})


class DeletePostView(DeleteView):
	model = Post
	template_name = 'posts/delete.html'
	success_url = reverse_lazy('dashboard')
	pk_url_kwarg = 'id'


# def detail_view(request, id):
# 	post = get_object_or_404(Post, pk=id)
# 	return render(request, 'posts/detail.html', {'post': post})


class DetailPostView(DetailView):
	model = Post
	template_name = 'posts/detail.html'
	pk_url_kwarg = 'id'


# def search_view(request):
# 	query = request.GET.get('q')
# 	posts = Post.objects.filter(title__icontains=query)
# 	return render(request, 'posts/all.html', {'posts': posts})


class SearhView(ListView):
	context_object_name = 'posts'
	model = Post
	template_name = 'posts/all.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Post.objects.filter(title__icontains=query)
		return object_list