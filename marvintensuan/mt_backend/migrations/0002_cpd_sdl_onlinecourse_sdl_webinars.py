from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('mt_backend', '0001_createsuperuser')]

    operations = [
        migrations.CreateModel(
            name='CPD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('thematic', models.CharField(max_length=5)),
                ('units', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cpd_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SDL_OnlineCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150)),
                ('facilitator', models.CharField(max_length=20)),
                ('onlinecourse_date_completed', models.DateField()),
                ('link_to_certificate', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SDL_Webinars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webinar_name', models.CharField(max_length=150)),
                ('organizer', models.CharField(max_length=20)),
                ('webinar_date', models.DateField()),
                ('html_desc', models.TextField()),
            ],
        ),
    ]
