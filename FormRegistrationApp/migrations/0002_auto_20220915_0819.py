# Generated by Django 3.1.1 on 2022-09-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormRegistrationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdata',
            name='informasi_mengenai_torche',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='materi',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='notes_for_tutor',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='sesi_hari',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='sesi_jam',
            field=models.TextField(),
        ),
    ]