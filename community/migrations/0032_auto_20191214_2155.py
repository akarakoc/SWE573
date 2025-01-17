# Generated by Django 2.2.6 on 2019-12-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0031_auto_20191214_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitytags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='communitytags',
            name='tagName',
            field=models.CharField(help_text='Enter Community Tag', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='datattypetags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='datattypetags',
            name='tagName',
            field=models.CharField(help_text='Enter Datatype Tag', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='usercircle',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='usertags',
            name='tagItem',
            field=models.CharField(help_text='Enter Community Tag Item', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='usertags',
            name='tagName',
            field=models.CharField(help_text='Enter Post Tag', max_length=2000, null=True),
        ),
    ]
