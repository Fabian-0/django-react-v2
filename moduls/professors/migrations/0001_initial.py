# Generated by Django 2.2.4 on 2021-06-30 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('avatar', models.URLField(max_length=255, null=True)),
                ('gender', models.CharField(choices=[('female', 'F'), ('male', 'M'), ('other', 'O')], max_length=6, null=True)),
                ('qualification', models.CharField(max_length=150, null=True)),
            ],
            options={
                'db_table': 'professors',
                'abstract': False,
            },
        ),
    ]
