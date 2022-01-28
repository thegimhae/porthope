from django.urls import path, include
from . import views
from .views import HomeView, AboutView, CategoryView, AnnoucementView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, EventView

urlpatterns = [

    # path('', views.home, name="home"),
    #path('<int:year>/<str:month>', views.home, name="home")
    path('', HomeView.as_view(), name = "home"),
    path('about/', AboutView.as_view(), name = "about"),
    path('announcement/', AnnoucementView.as_view(), name = "announcement"),
    path('post/<int:pk>',PostDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name = 'edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    # path('events', views.all_events, name="event_list"),
    path('events', EventView.as_view(), name="event_list"),
    # path('article/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment'),
]
