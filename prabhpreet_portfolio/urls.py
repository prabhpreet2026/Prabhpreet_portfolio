"""
URL configuration for prabhpreet_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('training/', views.training, name='training'),
    path('training/add/', views.add_training, name='add_training'),
    path('training/edit/<int:id>/', views.edit_training, name='edit_training'),
    path('training/delete/<int:id>/', views.delete_training, name='delete_training'),
    path('awards/', views.awards, name='awards'),
    path('awards/add/', views.add_award, name='add_award'),
    path('awards/edit/<int:id>/', views.edit_award, name='edit_award'),
    path('awards/delete/<int:id>/', views.delete_award, name='delete_award'),
    path('publications/', views.publications, name='publications'),
    path('publications/add/', views.add_publication, name='add_publication'),
    path('publications/edit/<int:id>/', views.edit_publication, name='edit_publication'),
    path('publications/delete/<int:id>/', views.delete_publication, name='delete_publication'),
    path('events/', views.events, name='events'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:id>/', views.delete_event, name='delete_event'),
    path('events/image/delete/<int:id>/', views.delete_event_image, name='delete_event_image'),
    path('research-trajectory/', views.research_trajectory, name='research_trajectory'),
    path('research-trajectory/add/', views.add_research_trajectory, name='add_research_trajectory'),
    path('research-trajectory/edit/<int:id>/', views.edit_research_trajectory, name='edit_research_trajectory'),
    path('research-trajectory/delete/<int:id>/', views.delete_research_trajectory, name='delete_research_trajectory'),
    path('research-areas/', views.research_areas, name='research_areas'),
    path('research-areas/add/', views.add_research_area, name='add_research_area'),
    path('research-areas/edit/<int:id>/', views.edit_research_area, name='edit_research_area'),
    path('research-areas/delete/<int:id>/', views.delete_research_area, name='delete_research_area'),
    path('statistics/', views.statistics, name='statistics'),
    path('statistics/add/', views.add_statistic, name='add_statistic'),
    path('statistics/edit/<int:id>/', views.edit_statistic, name='edit_statistic'),
    path('statistics/delete/<int:id>/', views.delete_statistic, name='delete_statistic'),
    path('profile/', views.profile, name='profile'),
    path('profile/add/', views.add_profile, name='add_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )