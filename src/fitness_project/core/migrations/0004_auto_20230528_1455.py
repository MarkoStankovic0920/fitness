# Generated by Django 3.2.19 on 2023-05-28 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('picture', models.ImageField(upload_to='picture')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
