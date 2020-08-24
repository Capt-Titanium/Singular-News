# Generated by Django 3.0.8 on 2020-08-16 04:47

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=10)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]