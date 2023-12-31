# Generated by Django 4.2.1 on 2023-07-13 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0024_qualimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfessionalExpertiseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('flag', models.IntegerField(default=0)),
                ('specilization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofession', to='MyApp.specializationmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofession', to='MyApp.userdetailsmodel')),
            ],
            options={
                'db_table': 'tbluser_professional_expertise',
                'ordering': ('description',),
            },
        ),
        migrations.CreateModel(
            name='ExperianceDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                'ordering': ('company_name',),
            },
        ),
    ]
