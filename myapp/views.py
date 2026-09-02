from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *

def sidebar(request):
    return render(request, "sidebar.html")

def training(request):
    trainings = Training.objects.all()
    context = {'trainings': trainings}
    return render(request, 'training.html', context)

def add_training(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        organizer = request.POST.get('organizer')
        year = request.POST.get('year')
        description = request.POST.get('description')
        certificate = request.FILES.get('certificate')
        Training.objects.create(title=title, organizer=organizer, year=year if year else None, description=description, certificate=certificate)
        return redirect('training')
    return render(request, 'training_form.html')

def edit_training(request, id):
    training = get_object_or_404(Training, id=id)
    if request.method == 'POST':
        training.title = request.POST.get('title')
        training.organizer = request.POST.get('organizer')
        year = request.POST.get('year')
        training.year = year if year else None
        training.description = request.POST.get('description')
        if request.FILES.get('certificate'):
            training.certificate = request.FILES.get('certificate')
        training.save()
        return redirect('training')
    context = {'training': training}
    return render(request, 'training_form.html', context)

def delete_training(request, id):
    training = get_object_or_404(Training, id=id)
    if request.method == 'POST':
        training.delete()
        return redirect('training')
    return render(request, 'training_delete.html', {'training': training})



def awards(request):
    awards = Award.objects.all()
    return render(request, 'awards.html', {'awards': awards})

def add_award(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        title = request.POST.get('title')
        awarding_body = request.POST.get('awarding_body')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        is_active = request.POST.get('is_active') == 'on'
        order = request.POST.get('order') or 0
        Award.objects.create(year=year, title=title, awarding_body=awarding_body, description=description, image=image, is_active=is_active, order=order)
        return redirect('awards')
    return render(request, 'award_form.html')

def edit_award(request, id):
    award = get_object_or_404(Award, id=id)
    if request.method == 'POST':
        award.year = request.POST.get('year')
        award.title = request.POST.get('title')
        award.awarding_body = request.POST.get('awarding_body')
        award.description = request.POST.get('description')
        award.is_active = request.POST.get('is_active') == 'on'
        award.order = request.POST.get('order') or 0
        if request.FILES.get('image'):
            award.image = request.FILES.get('image')
        award.save()
        return redirect('awards')
    return render(request, 'award_form.html', {'award': award})

def delete_award(request, id):
    award = get_object_or_404(Award, id=id)
    if request.method == 'POST':
        award.delete()
        return redirect('awards')
    return render(request, 'award_delete.html', {'award': award})



def publications(request):
    publications = Publication.objects.all()
    return render(request, 'publications.html', {'publications': publications})

def add_publication(request):
    if request.method == 'POST':
        Publication.objects.create(
            title=request.POST.get('title'),
            authors=request.POST.get('authors'),
            publication_type=request.POST.get('publication_type'),
            journal_or_venue=request.POST.get('journal_or_venue'),
            publication_year=request.POST.get('publication_year'),
            doi=request.POST.get('doi') or None,
            scopus_indexed=request.POST.get('scopus_indexed') == 'on',
            citation_count=request.POST.get('citation_count') or 0,
            abstract=request.POST.get('abstract'),
            is_top_publication=request.POST.get('is_top_publication') == 'on',
            is_recent=request.POST.get('is_recent') == 'on',
            is_active=request.POST.get('is_active') == 'on'
        )
        return redirect('publications')
    return render(request, 'publication_form.html')

def edit_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        publication.title = request.POST.get('title')
        publication.authors = request.POST.get('authors')
        publication.publication_type = request.POST.get('publication_type')
        publication.journal_or_venue = request.POST.get('journal_or_venue')
        publication.publication_year = request.POST.get('publication_year')
        publication.doi = request.POST.get('doi') or None
        publication.scopus_indexed = request.POST.get('scopus_indexed') == 'on'
        publication.citation_count = request.POST.get('citation_count') or 0
        publication.abstract = request.POST.get('abstract')
        publication.is_top_publication = request.POST.get('is_top_publication') == 'on'
        publication.is_recent = request.POST.get('is_recent') == 'on'
        publication.is_active = request.POST.get('is_active') == 'on'
        publication.save()
        return redirect('publications')
    return render(request, 'publication_form.html', {'publication': publication})

def delete_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        publication.delete()
        return redirect('publications')
    return render(request, 'publication_delete.html', {'publication': publication})


def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        event = Event.objects.create(
            title=request.POST.get('title'),
            event_type=request.POST.get('event_type'),
            description=request.POST.get('description'),
            event_date=request.POST.get('event_date') or None,
            cover_image=request.FILES.get('cover_image'),
            is_active=request.POST.get('is_active') == 'on',
            order=request.POST.get('order') or 0
        )
        images = request.FILES.getlist('gallery_images')
        captions = request.POST.getlist('captions')
        for i, image in enumerate(images):
            caption = captions[i] if i < len(captions) else ''
            EventImage.objects.create(event=event, image=image, caption=caption, order=i)
        return redirect('events')
    return render(request, 'event_form.html')

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.event_type = request.POST.get('event_type')
        event.description = request.POST.get('description')
        event.event_date = request.POST.get('event_date') or None
        event.is_active = request.POST.get('is_active') == 'on'
        event.order = request.POST.get('order') or 0
        if request.FILES.get('cover_image'):
            event.cover_image = request.FILES.get('cover_image')
        event.save()
        images = request.FILES.getlist('gallery_images')
        captions = request.POST.getlist('captions')
        for i, image in enumerate(images):
            caption = captions[i] if i < len(captions) else ''
            EventImage.objects.create(event=event, image=image, caption=caption, order=i)
        return redirect('events')
    return render(request, 'event_form.html', {'event': event})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    return render(request, 'event_delete.html', {'event': event})

def delete_event_image(request, id):
    image = get_object_or_404(EventImage, id=id)
    event_id = image.event.id
    if request.method == 'POST':
        image.delete()
    return redirect('edit_event', id=event_id)


def research_trajectory(request):
    trajectories = ResearchTrajectory.objects.all()
    return render(request, 'research_trajectory.html', {'trajectories': trajectories})

def add_research_trajectory(request):
    if request.method == 'POST':
        ResearchTrajectory.objects.create(
            year=request.POST.get('year'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            order=request.POST.get('order') or 0,
            is_active=request.POST.get('is_active') == 'on'
        )
        return redirect('research_trajectory')
    return render(request, 'research_trajectory_form.html')

def edit_research_trajectory(request, id):
    trajectory = get_object_or_404(ResearchTrajectory, id=id)
    if request.method == 'POST':
        trajectory.year = request.POST.get('year')
        trajectory.title = request.POST.get('title')
        trajectory.description = request.POST.get('description')
        trajectory.order = request.POST.get('order') or 0
        trajectory.is_active = request.POST.get('is_active') == 'on'
        trajectory.save()
        return redirect('research_trajectory')
    return render(request, 'research_trajectory_form.html', {'trajectory': trajectory})

def delete_research_trajectory(request, id):
    trajectory = get_object_or_404(ResearchTrajectory, id=id)
    if request.method == 'POST':
        trajectory.delete()
        return redirect('research_trajectory')
    return render(request, 'research_trajectory_delete.html', {'trajectory': trajectory})

def research_areas(request):
    areas = ResearchArea.objects.all()
    return render(request, 'research_areas.html', {'areas': areas})

def add_research_area(request):
    if request.method == 'POST':
        ResearchArea.objects.create(
            name=request.POST.get('name'),
            is_active=request.POST.get('is_active') == 'on'
        )
        return redirect('research_areas')
    return render(request, 'research_area_form.html')

def edit_research_area(request, id):
    area = get_object_or_404(ResearchArea, id=id)
    if request.method == 'POST':
        area.name = request.POST.get('name')
        area.is_active = request.POST.get('is_active') == 'on'
        area.save()
        return redirect('research_areas')
    return render(request, 'research_area_form.html', {'area': area})

def delete_research_area(request, id):
    area = get_object_or_404(ResearchArea, id=id)
    if request.method == 'POST':
        area.delete()
        return redirect('research_areas')
    return render(request, 'research_area_delete.html', {'area': area})


def statistics(request):
    statistics = Statistic.objects.all()
    return render(request, 'statistics.html', {'statistics': statistics})

def add_statistic(request):
    if request.method == 'POST':
        Statistic.objects.create(
            title=request.POST.get('title'),
            value=request.POST.get('value'),
            description=request.POST.get('description'),
            order=request.POST.get('order') or 0,
            is_active=request.POST.get('is_active') == 'on'
        )
        return redirect('statistics')
    return render(request, 'statistic_form.html')

def edit_statistic(request, id):
    statistic = get_object_or_404(Statistic, id=id)
    if request.method == 'POST':
        statistic.title = request.POST.get('title')
        statistic.value = request.POST.get('value')
        statistic.description = request.POST.get('description')
        statistic.order = request.POST.get('order') or 0
        statistic.is_active = request.POST.get('is_active') == 'on'
        statistic.save()
        return redirect('statistics')
    return render(request, 'statistic_form.html', {'statistic': statistic})

def delete_statistic(request, id):
    statistic = get_object_or_404(Statistic, id=id)
    if request.method == 'POST':
        statistic.delete()
        return redirect('statistics')
    return render(request, 'statistic_delete.html', {'statistic': statistic})




def profile(request):
    profile = Profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})

def add_profile(request):
    if request.method == 'POST':
        Profile.objects.create(
            name=request.POST.get('name'),
            designation=request.POST.get('designation'),
            department=request.POST.get('department'),
            university=request.POST.get('university'),
            email=request.POST.get('email'),
            alternate_email=request.POST.get('alternate_email'),
            profile_image=request.FILES.get('profile_image'),
            short_intro=request.POST.get('short_intro'),
            biography=request.POST.get('biography'),
            research_vision=request.POST.get('research_vision')
        )
        return redirect('profile')
    return render(request, 'profile_form.html')

def edit_profile(request):
    profile = get_object_or_404(Profile, id=Profile.objects.first().id)
    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.designation = request.POST.get('designation')
        profile.department = request.POST.get('department')
        profile.university = request.POST.get('university')
        profile.email = request.POST.get('email')
        profile.alternate_email = request.POST.get('alternate_email')
        profile.short_intro = request.POST.get('short_intro')
        profile.biography = request.POST.get('biography')
        profile.research_vision = request.POST.get('research_vision')
        if request.FILES.get('profile_image'):
            profile.profile_image = request.FILES.get('profile_image')
        profile.save()
        return redirect('profile')
    return render(request, 'profile_form.html', {'profile': profile})

def delete_profile(request):
    profile = get_object_or_404(Profile, id=Profile.objects.first().id)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile')
    return render(request, 'profile_delete.html', {'profile': profile})


def dashboard(request):
    context = {
        'profile_count': Profile.objects.count(),
        'training_count': Training.objects.count(),
        'award_count': Award.objects.count(),
        'publication_count': Publication.objects.count(),
        'event_count': Event.objects.count(),
        'trajectory_count': ResearchTrajectory.objects.count(),
        'area_count': ResearchArea.objects.count(),
        'statistic_count': Statistic.objects.count(),
    }
    return render(request, 'dashboard.html', context)

def home(request):
    profile = Profile.objects.first()
    statistics = Statistic.objects.filter(is_active=True).order_by('order')
    research_trajectory = ResearchTrajectory.objects.filter(is_active=True).order_by('-id')
    research_areas = ResearchArea.objects.filter(is_active=True)
    events = Event.objects.filter(is_active=True).order_by('order', '-event_date')
    publications = Publication.objects.filter(is_active=True).order_by('-publication_year')
    top_publications = Publication.objects.filter(is_active=True, is_top_publication=True).order_by('-publication_year')[:5]
    recent_publications = Publication.objects.filter(is_active=True, is_recent=True).order_by('-publication_year')
    awards = Award.objects.filter(is_active=True).order_by('-year', 'order')
    trainings = Training.objects.filter(is_active=True).order_by('-year')

    return render(request, 'index.html', {'profile': profile, 'statistics': statistics, 'research_trajectory': research_trajectory, 'research_areas': research_areas, 'events': events, 'publications': publications, 'top_publications': top_publications, 'recent_publications': recent_publications, 'awards': awards, 'trainings': trainings})
