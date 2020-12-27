from django.db import models

class CPD(models.Model):
    name = models.CharField(max_length=150)
    thematic = models.CharField(max_length=5)
    units = models.DecimalField(max_digits=3, decimal_places=2)
    cpd_date = models.DateField()

class SDL_Webinars(models.Model):
    webinar_name = models.CharField(max_length=150)
    organizer = models.CharField(max_length=20)
    webinar_date = models.DateField()
    html_desc = models.TextField()

class SDL_OnlineCourse(models.Model):
    course_name = models.CharField(max_length=150)
    facilitator = models.CharField(max_length=20)
    onlinecourse_date_completed = models.DateField()
    link_to_certificate = models.URLField()
