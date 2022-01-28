from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Event
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# from calendar import HTMLCalandar

# Create your views here.
# def home(request, 'home.html'):

# # TODO: Figure out how to use the function

# def all_events(request):
#     event_list = Event.objects.all()
#     return render(request, 'event_list.html',
#       {'event_list': event_list})

# def home(request, year, month)
#      name = "john"
#     return render(request, 'home.html',{
#    '#name'
#        month_number
#        "year": year
#        "month": month})



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['post_date']
#   ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})

class AboutView(TemplateView):
    template_name = 'about.html'

class AnnoucementView(TemplateView):
    template_name = 'annoucement.html'

class EventView(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_list.html'
    success_url = reverse_lazy('home')
    # event_list = Event.objects.all()
    # return render(request, 'event_list.html',
    #   {'event_list': event_list})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    success_url = reverse_lazy('home')

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'
    #fields = ('title','body')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    #fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    success_url = reverse_lazy('home')
    # fields = ('title','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# class AddCommentView(CreateView):
#     model = Category
#     form_class = PostForm
#     template_name = 'add_comment.html'
#     success_url = reverse_lazy('home')
    #fields = '__all__'
    #fields = ('title','body')
