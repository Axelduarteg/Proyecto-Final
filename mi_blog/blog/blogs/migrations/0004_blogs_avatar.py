# Generated by Django 4.2.1 on 2023-05-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blogs_image_blogs_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='avatar',
            field=models.ImageField(default='blog_imagen/default_imagen.jpg', upload_to='blog_imagen/'),
        ),
    ]