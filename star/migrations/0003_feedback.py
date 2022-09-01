# Generated by Django 4.1 on 2022-08-31 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0002_remove_testimonials_user_testimonials_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='star.courses')),
            ],
        ),
    ]