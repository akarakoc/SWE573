# Generated by Django 2.2.6 on 2019-11-08 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_auto_20191108_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postsTag', to='community.Datatypes')),
            ],
        ),
        migrations.CreateModel(
            name='DatatTypeTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatypeTag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dataTag', to='community.Datatypes')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communityTag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commTag', to='community.Communities')),
            ],
        ),
    ]