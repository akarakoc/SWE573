# Generated by Django 2.2.6 on 2019-11-07 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_auto_20191107_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='postCreationDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='postCreator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postcreator', to='community.communityUsers'),
        ),
        migrations.AddField(
            model_name='posts',
            name='relatedCommunityforPost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postCommunity', to='community.Communities'),
        ),
        migrations.AddField(
            model_name='posts',
            name='relatedDatatypes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='relatedDatatype', to='community.Datatypes'),
        ),
        migrations.AlterField(
            model_name='datatypefields',
            name='fieldCreator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fieldsCreator', to='community.communityUsers'),
        ),
    ]
