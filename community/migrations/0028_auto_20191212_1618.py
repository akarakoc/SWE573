# Generated by Django 2.2.6 on 2019-12-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0027_auto_20191210_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitytags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='datattypetags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='posttags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usercircle',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usertags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=200, null=True),
        ),
    ]