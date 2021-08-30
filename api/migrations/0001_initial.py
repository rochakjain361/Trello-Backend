# Generated by Django 3.2.6 on 2021-08-30 09:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('card_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('enrollment_no', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('admin', models.BooleanField()),
                ('enabled', models.BooleanField()),
                ('token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('wiki', ckeditor.fields.RichTextField()),
                ('due_date', models.DateField()),
                ('admins', models.ManyToManyField(related_name='admins_project', to='api.user')),
                ('members', models.ManyToManyField(related_name='member', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='assigned',
            field=models.ManyToManyField(to='api.user'),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.list'),
        ),
    ]
