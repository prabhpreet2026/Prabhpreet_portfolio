from django.db import models

# Create your models here.
from django.db import models


# -----------------------------------
# SITE / PERSONAL INFORMATION
# -----------------------------------

class Profile(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=300)
    university = models.CharField(max_length=300)

    email = models.EmailField()
    alternate_email = models.EmailField(blank=True)

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    short_intro = models.TextField()
    biography = models.TextField()

    research_vision = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# -----------------------------------
# STATISTICS / RECORD
# -----------------------------------

class Statistic(models.Model):
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.value}"

    class Meta:
        ordering = ['order']


# -----------------------------------
# RESEARCH TRAJECTORY
# -----------------------------------

class ResearchTrajectory(models.Model):
    year = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField()

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} - {self.title}"

    class Meta:
        ordering = ['order']


# -----------------------------------
# RESEARCH AREAS / KEYWORDS
# -----------------------------------

class ResearchArea(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# -----------------------------------
# EVENTS
# -----------------------------------

class Event(models.Model):
    EVENT_TYPES = [
        ('book', 'Book Publication'),
        ('lecture', 'Guest Talk / Lecture'),
        ('evaluation', 'Academic Evaluation'),
        ('conference', 'Conference Chair'),
        ('fdp', 'Faculty Refresher'),
        ('workshop', 'AI Workshop'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=300)
    event_type = models.CharField( max_length=50,choices=EVENT_TYPES,default='other')
    description = models.TextField(blank=True)
    event_date = models.DateField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='events/',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-event_date']


# -----------------------------------
# EVENT GALLERY
# -----------------------------------

class EventImage(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='events/gallery/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.event.title} - Image"


# -----------------------------------
# PUBLICATIONS
# -----------------------------------

class Publication(models.Model):
    PUBLICATION_TYPES = [
        ('journal', 'Journal Article'),
        ('conference', 'Conference Paper'),
        ('book', 'Book Chapter'),
        ('book', 'Book'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=500)
    authors = models.TextField()
    publication_type = models.CharField(max_length=50,choices=PUBLICATION_TYPES,default='journal')
    journal_or_venue = models.CharField(max_length=500,blank=True)
    publication_year = models.PositiveIntegerField()
    doi = models.URLField(blank=True,null=True)
    scopus_indexed = models.BooleanField(default=False)
    citation_count = models.PositiveIntegerField(default=0)
    abstract = models.TextField(blank=True)
    is_top_publication = models.BooleanField(default=False)
    is_recent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_year']

# -----------------------------------
# AWARDS / DISTINCTIONS
# -----------------------------------

class Award(models.Model):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=300)
    awarding_body = models.CharField(max_length=300,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='awards/',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.year} - {self.title}"

    class Meta:
        ordering = ['-year', 'order']

class Training(models.Model):
    title = models.CharField(max_length=300)
    organizer = models.CharField(max_length=300,blank=True)
    year = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(blank=True)
    certificate = models.ImageField(upload_to='training/',blank=True,null=True)
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-year']