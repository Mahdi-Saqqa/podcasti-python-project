# Generated by Django 4.2 on 2023-04-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_podcast_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.FileField(null=True, upload_to='profiles_picture/'),
        ),
    ]
