# Generated by Django 3.2.8 on 2021-10-17 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('story_points', models.IntegerField(blank=True, null=True)),
                ('business_value', models.IntegerField(blank=True, null=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.list')),
            ],
        ),
    ]
