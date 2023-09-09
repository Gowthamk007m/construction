# Generated by Django 4.1.7 on 2023-03-30 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=25, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_profiles/')),
            ],
        ),
        migrations.CreateModel(
            name='Site_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('site_role', models.CharField(choices=[('Sitehead', 'Sitehead'), ('Superviser', 'Superviser'), ('Technician', 'Technician')], max_length=50)),
                ('image', models.ImageField(null=True, upload_to='profile_images/')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Site_data.users')),
            ],
        ),
        migrations.CreateModel(
            name='Construction_Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='site_profiles/')),
                ('num_workers', models.IntegerField(blank=True, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('working_status', models.CharField(choices=[('Working', 'Working'), ('Halted', 'Halted'), ('Completed', 'Completed')], max_length=50)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('superviser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site_data.site_user')),
            ],
        ),
    ]