from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
	model = models.Article
	template_name = 'article_list.html'
	login_url = 'login'

class ArticleDetailView(LoginRequiredMixin, DetailView):
	model = models.Article
	template_name = 'article_detail.html'
	login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Article
	fields = ['title', 'body', ]
	template_name = 'article_edit.html'
	login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Article
	template_name = 'article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'

class ArticleCreateView(LoginRequiredMixin, CreateView): #use this mixin to only allow loggedin users to create posts
	model = models.Article
	template_name = 'article_new.html'
	fields = ['title', 'body', ] #removed author from fields and created below function for authorisation
	login_url = 'login' #overrides default login page to get redirected to from accounts/login to users/login, where our login page is
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
