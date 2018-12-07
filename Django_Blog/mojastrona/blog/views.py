#Więcej o wbudowanych klasa
#https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.forms import PostForm, KomentarzForm
from django.urls import reverse_lazy
# importowanie CRUD'a
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from blog.models import Post, Komentarz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#dekoratory pozwalaja na uzycie danej metody tylko i wylacznie gdy dekorator uzytkowniak jest zgodny z dekoratorem metody

#The login_required decorator¶
#login_required(redirect_field_name='next', login_url=None)[source]¶
#As a shortcut, you can use the convenient login_required() decorator:

#login_required() does the following:

 # If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Example: /accounts/login/?next=/polls/3/.
 #- If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.

#"""


"""
The LoginRequiredMixin

This mixin is rather simple and is generally the first inherited class in any of our views.
If we don’t have an authenticated user there’s no need to go any further.
If you’ve used Django before you are probably familiar with the login_required decorator.
All we are doing here is requiring a user to be authenticated to be able to get to this view.
If a view is using this mixin, all requests by non-authenticated users will be redirected to the login page or shown an HTTP 403 Forbidden error,
depending on the raise_exception parameter.


"""


# Create your views here.
#strona o nas
class About(TemplateView):
    template_name = 'about.html'


#
class PostList(ListView):
    model = Post

# Utworzenie zapytania (query) na wzór SQL porzodkujące posty według daty publikacji
# __lte = less than or equal to <=
# '-data_publikacji' porządek według daty malejąco 'descending'
# https://docs.djangoproject.com/en/2.0/topics/db/queries/#field-lookups
    def get_queryset(self):
        return Post.objects.filter(data_publikacji__lte=timezone.now()).order_by('-data_publikacji')

#Tworzenie CRUD'a

class PostDetail (DetailView):
    model = Post


class UtworzPost(LoginRequiredMixin, CreateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePost(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post



class UsuwaniePostu(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = reverse_lazy('post_list')

#nie jest mi to potrzebne chyba
class DraftlistView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
#query sprawdza czy napisany post ma date publikacji jeśli jest wartość null=True wtedy przechowuje je w drafcie
    def get_queryset(self):
        return Post.objects.filter(data_publikacji__isnull=True).order_by('data_utworzenia')


##########################################################################
#              Dodawanie, usuwanie i edytowanie komentarzy               #
##########################################################################

@login_required
def dodawanie_komentarzy(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = KomentarzForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = KomentarzForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def zatwierdzanie_komentarzy(request, pk):
    comment = get_object_or_404(Komentarz, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

#"""comment.approve() odwoluje się do metody z klasy Komentarz:
#
#    def approve(self):
#        self.approved = True
#        self.save()
#
#"""

#"""
#pk=comment.post.pk odwołuje sie się do:
#
#class Komentarz(models.Model):
#    post = models.ForeignKey

#post odwołuje się do klucza głównego z klasy Post
#"""



@login_required
def usuwanie_komentarzy(request, pk):
    comment = get_object_or_404(Komentarz, pk=pk)
# nowa zmienna pojawia się w celu usunięcia komentarza i poźniejszego odniesienia się do pk
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
