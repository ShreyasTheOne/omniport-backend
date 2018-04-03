# Generated by Django 2.0.3 on 2018-04-01 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_DEPARTMENT_MODEL),
        ('shell', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=127)),
                ('semester_count', models.IntegerField(blank=True, null=True)),
                ('degree', models.CharField(choices=[('btech', 'B.Tech. - Bachelor of Technology'), ('idd', 'Int. M.Tech. - Integrated Dual Degree'), ('bsc', 'B.Sc. - Bachelor of Science'), ('imsc', 'Int. M.Sc. - Integrated Master of Science'), ('barch', 'B.Arch. - Bachelor of Architecture'), ('mtech', 'M.Tech. - Master of Technology'), ('msc', 'M.Sc. - Master of Science'), ('march', 'M.Arch. - Master of Architecture'), ('murp', 'M.U.R.P - Master of Urban and Regional Planning'), ('pgdip', 'P.G. Dip. - Post-graduate Diploma'), ('mba', 'M.B.A. - Master of Business Administration'), ('mca', 'M.C.A. - Master of Computer Applications'), ('phd', 'Ph.D. - Doctor of Philosophy'), ('pdoc', 'Post Doc. - Post-doctorate')], max_length=7, unique=True)),
            ],
            options={
                'verbose_name_plural': 'branches',
            },
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(choices=[('ahec', 'Alternate Hydro Energy Centre'), ('cnt', 'Centre for Nanotechnology'), ('cedmm', 'Centre of Excellence in Disaster Mitigation and Management'), ('cts', 'Centre for Transportation Systems'), ('chs', 'Centre for Himalayan Studies'), ('ceudm', 'Centre of Excellence in Urban Design and Management'), ('mgcl', 'Mahatma Gandhi Central Library'), ('cec', 'Continuing Education Centre'), ('icc', 'Institute Computer Centre'), ('iic', 'Institute Instrumentation Centre'), ('iprc', 'Intellectual Property Rights Cell'), ('etc', 'Education Technology Cell'), ('ih', 'Institute Hospital'), ('tides', 'Tides Incubation Centre')], max_length=7, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(choices=[('ased', 'Applied Science and Engineering Department'), ('arcd', 'Architecture and Planning Department'), ('btd', 'Biotechnology Department'), ('ched', 'Chemical Engineering Department'), ('cyd', 'Chemistry Department'), ('ced', 'Civil Engineering Department'), ('csed', 'Computer Science and Engineering Department'), ('esd', 'Earth Sciences Department'), ('eqd', 'Earthquake Department'), ('eed', 'Electrical Engineering Department'), ('eced', 'Electronics and Communication Engineering Department'), ('hsd', 'Humanities and Social Sciences Department'), ('hyd', 'Hydrology Department'), ('msd', 'Management Studies Department'), ('mad', 'Mathematics Department'), ('mied', 'Mechanical and Industrial Engineering Department'), ('mmed', 'Metallurgical and Materials Engineering Department'), ('ptd', 'Paper Technology Department'), ('phd', 'Physics Department'), ('pped', 'Polymer and Process Engineering Department'), ('wrdmd', 'Water Resources Development and Management Department'), ('qip', 'Quality Improvement Programme')], max_length=7, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_DEPARTMENT_MODEL),
        ),
    ]