# Generated by Django 4.2.1 on 2023-07-13 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_admindetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodePostModel',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('question', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.IntegerField(default=0)),
                ('flag', models.IntegerField(default=0)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codepost', to='MyApp.contentmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codepost', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tblcode_post_s',
                'ordering': ('post_id',),
            },
        ),
    ]
