# Generated by Django 4.0.6 on 2022-08-10 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_model',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ip_model',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Blogger_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('profile_pic', models.ImageField(upload_to='Blogger_Profile')),
                ('profession', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blogs',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogger_profile'),
        ),
    ]
