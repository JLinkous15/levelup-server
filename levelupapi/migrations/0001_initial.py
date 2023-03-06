# Generated by Django 4.1.6 on 2023-03-06 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('creator', models.CharField(max_length=50)),
                ('number_of_players', models.IntegerField(default=1)),
                ('skill_level', models.CharField(default='Easy', max_length=8)),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GameType_Games', to='levelupapi.gametype')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('attendance', models.ManyToManyField(through='levelupapi.Attendance', to='levelupapi.gamer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_games', to='levelupapi.game')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='levelupapi.gamer')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Event_attendance', to='levelupapi.event'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attendees', to='levelupapi.gamer'),
        ),
    ]
