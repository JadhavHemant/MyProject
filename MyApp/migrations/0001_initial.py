# Generated by Django 4.2.1 on 2023-07-13 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitysModel',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblcitys',
                'ordering': ('city_id',),
            },
        ),
        migrations.CreateModel(
            name='DesignationModel',
            fields=[
                ('designation_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tbldesignations',
                'ordering': ('designation_id',),
            },
        ),
        migrations.CreateModel(
            name='GenderModel',
            fields=[
                ('gender_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblgenders',
                'ordering': ('gender_id',),
            },
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='MyApp.citysmodel')),
            ],
            options={
                'db_table': 'tbllocations',
                'ordering': ('location_id',),
            },
        ),
        migrations.CreateModel(
            name='Postcategories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100, null=True, unique=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblpostcategories',
                'ordering': ('category_id',),
            },
        ),
        migrations.CreateModel(
            name='QualificationModel',
            fields=[
                ('qualification_id', models.AutoField(primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=100, null=True, unique=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblqualifications',
                'ordering': ('qualification_id',),
            },
        ),
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblrole',
                'ordering': ('role_id',),
            },
        ),
        migrations.CreateModel(
            name='SpecializationModel',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('specialization', models.CharField(max_length=100, null=True, unique=True)),
                ('flag', models.IntegerField(default=0)),
                ('qualification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special', to='MyApp.qualificationmodel')),
            ],
            options={
                'db_table': 'tblspecializations',
                'ordering': ('specialization_id',),
            },
        ),
        migrations.CreateModel(
            name='StatesModel',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_Name', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblstates',
                'ordering': ('state_id',),
            },
        ),
        migrations.CreateModel(
            name='TopicsModel',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100, null=True, unique=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tbltopics',
                'ordering': ('topic_id',),
            },
        ),
        migrations.CreateModel(
            name='UserDetailsModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('local_address', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('joining_date', models.DateField()),
                ('user_photo', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('emial_address', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('is_premium', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=100)),
                ('flag', models.IntegerField(default=0)),
                ('gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdetails', to='MyApp.gendermodel')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdetails', to='MyApp.locationmodel')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdetails', to='MyApp.rolemodel')),
            ],
            options={
                'db_table': 'tbluser_details',
                'ordering': ('first_name',),
            },
        ),
        migrations.CreateModel(
            name='UserProfessionalExpertiseModel',
            fields=[
                ('expertise_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
                ('specilization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofession', to='MyApp.specializationmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofession', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tbluser_professional_expertise',
                'ordering': ('expertise_id',),
            },
        ),
        migrations.CreateModel(
            name='UserPostModel',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_date', models.DateField()),
                ('post_title', models.CharField(max_length=100)),
                ('post_description', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('is_active', models.IntegerField(default=0)),
                ('flag', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userpost', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tbluser_posts',
                'ordering': ('post_id',),
            },
        ),
        migrations.CreateModel(
            name='QualiModel',
            fields=[
                ('user_qualification_id', models.AutoField(primary_key=True, serialize=False)),
                ('university', models.CharField(max_length=100)),
                ('passing_year', models.ImageField(upload_to='')),
                ('medium', models.CharField(max_length=100)),
                ('percentage', models.FloatField()),
                ('flag', models.IntegerField(default=0)),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifiaction', to='MyApp.specializationmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifiaction', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tbluser_qualifications',
                'ordering': ('university',),
            },
        ),
        migrations.CreateModel(
            name='PostLikesDislikesModel',
            fields=[
                ('like_dislike_id', models.AutoField(primary_key=True, serialize=False)),
                ('like_dislike_date', models.DateField()),
                ('is_like', models.IntegerField(default=0)),
                ('flag', models.IntegerField(default=0)),
                ('like_dislike_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likedislike', to='MyApp.userdetailsmodel')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likedislike', to='MyApp.userpostmodel')),
            ],
            options={
                'db_table': 'tbl_post_dis_likes',
                'ordering': ('like_dislike_id',),
            },
        ),
        migrations.CreateModel(
            name='PostCommentsModel',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_date', models.DateField()),
                ('comment_message', models.CharField(max_length=255)),
                ('comment_photo', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
                ('comment_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcomments', to='MyApp.userdetailsmodel')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcomment', to='MyApp.userpostmodel')),
            ],
            options={
                'db_table': 'tbpost_comments',
                'ordering': ('comment_id',),
            },
        ),
        migrations.CreateModel(
            name='PostCommentReplymodel',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('reply_date', models.DateField()),
                ('reply_mesage', models.CharField(max_length=100)),
                ('comment_photo', models.CharField(max_length=100)),
                ('flag', models.IntegerField(default=0)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentreply', to='MyApp.postcommentsmodel')),
                ('reply_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentreply', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tbpost_comment_replys',
                'ordering': ('reply_id',),
            },
        ),
        migrations.CreateModel(
            name='ExperianceDetailsModel',
            fields=[
                ('experience_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('from_year', models.DateField()),
                ('to_year', models.DateField()),
                ('job_descrption', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
                ('designation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExperianceDetails', to='MyApp.designationmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExperianceDetails', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tblexperience_details',
                'ordering': ('experience_id',),
            },
        ),
        migrations.CreateModel(
            name='ContentModel',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('content_name', models.CharField(max_length=100, null=True)),
                ('flag', models.IntegerField(default=0)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='MyApp.topicsmodel')),
            ],
            options={
                'db_table': 'tbltopiccontents',
                'ordering': ('content_id',),
            },
        ),
        migrations.AddField(
            model_name='citysmodel',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cityname', to='MyApp.statesmodel'),
        ),
    ]
