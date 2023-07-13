# Generated by Django 4.2.1 on 2023-07-13 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0029_postcomment_postlikesdislikestbmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateField()),
                ('comment_message', models.CharField(max_length=255)),
                ('comment_photo', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
                ('comment_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentpost', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'post_comments_tbl',
                'ordering': ('comment_message',),
            },
        ),
        migrations.CreateModel(
            name='JobOpeningsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_date', models.DateField()),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('experience_required', models.CharField(max_length=255)),
                ('job_description', models.CharField(max_length=255)),
                ('is_active', models.ImageField(default=0, upload_to='')),
                ('flag', models.ImageField(default=0, upload_to='')),
                ('opening_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tbljob_openings',
                'ordering': ('company_name',),
            },
        ),
        migrations.CreateModel(
            name='UpdateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField()),
                ('update_title', models.CharField(max_length=100)),
                ('update_desription', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tbl_update',
                'ordering': ('update_date',),
            },
        ),
        migrations.CreateModel(
            name='PostLikesSharesTableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_date', models.DateField()),
                ('flag', models.IntegerField(default=0)),
                ('opening_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesharepost', to='MyApp.jobopeningsmodel')),
                ('share_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesharepost', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'post_likes_shares_tbl',
                'ordering': ('share_date',),
            },
        ),
        migrations.CreateModel(
            name='PostDislikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_dislike_date', models.DateField()),
                ('is_like', models.IntegerField(default=0)),
                ('flag', models.IntegerField(default=0)),
                ('like_dislike_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postdislike', to='MyApp.userdetailsmodel')),
                ('opening_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postdislike', to='MyApp.jobopeningsmodel')),
            ],
            options={
                'db_table': 'post_likes_dislikes_tbl',
                'ordering': ('like_dislike_date',),
            },
        ),
        migrations.CreateModel(
            name='CommentPostReplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_date', models.DateField()),
                ('reply_mesage', models.CharField(max_length=255)),
                ('comment_photo', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replypost', to='MyApp.commentpostmodel')),
                ('reply_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replypost', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'post_comment_replys_tbl',
                'ordering': ('reply_date',),
            },
        ),
        migrations.AddField(
            model_name='commentpostmodel',
            name='opening_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentpost', to='MyApp.jobopeningsmodel'),
        ),
    ]
