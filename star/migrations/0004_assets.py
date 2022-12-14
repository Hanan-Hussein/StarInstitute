# Generated by Django 4.1 on 2022-09-02 06:20

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='logo')),
                ('hero_desktop', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='hero_desktop')),
                ('hero_mobile', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='hero_mobile')),
                ('hero_svg1', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Hero_svg_1')),
                ('hero_svg2', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Hero_svg_2')),
                ('hero_svg3', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Hero_svg_3')),
                ('hero_svg4', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Hero_svg_4')),
                ('hero_svg5', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Hero_svg_5')),
                ('about_mobile', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='about_mobile')),
                ('about_desktop', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='about_desktop')),
                ('contact', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='contact')),
            ],
        ),
    ]
