# Generated by Django 4.2.1 on 2023-07-13 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLikesSharesModel',
            fields=[
                ('share_id', models.AutoField(primary_key=True, serialize=False)),
                ('share_date', models.DateField()),
                ('flag', models.IntegerField(default=0)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesshares', to='MyApp.userpostmodel')),
                ('share_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesshares', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tblpost_likes_shares',
                'ordering': ('share_id',),
            },
        ),
    ]
