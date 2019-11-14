# Generated by Django 2.2.6 on 2019-11-08 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0015_auto_20191108_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(help_text='Enter Post Tag', max_length=200, null=True)),
                ('userTag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usersTag', to='community.communityUsers')),
            ],
        ),
        migrations.CreateModel(
            name='UserCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circleOwner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.communityUsers')),
                ('circleUsers', models.ManyToManyField(help_text='Select Members', related_name='Followers', to='community.communityUsers')),
            ],
        ),
    ]