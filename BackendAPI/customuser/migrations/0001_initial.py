# Generated by Django 2.2.7 on 2020-01-02 23:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_column='usu_des_email', max_length=255, unique=True, verbose_name='e-mail')),
                ('is_active', models.BooleanField(db_column='usu_idc_ativo', default=True, verbose_name='ativo')),
                ('is_admin', models.BooleanField(db_column='usu_idc_admin', default=False, verbose_name='admin')),
                ('jwt_secret', models.UUIDField(db_column='usu_uid_jwtsecret', default=uuid.uuid4, verbose_name='JWT Secret')),
                ('is_blocked', models.BooleanField(db_column='usu_idc_bloqueado', default=False, verbose_name='bloqueado')),
                ('is_staff', models.BooleanField(db_column='usu_idc_staff', default=False, verbose_name='is staff')),
                ('phone', models.CharField(blank=True, db_column='usu_des_telefone', max_length=11, null=True, verbose_name='telefone')),
                ('photo', models.ImageField(blank=True, db_column='usu_img_foto', null=True, upload_to='photos', verbose_name='foto')),
            ],
            options={
                'db_table': 'usuario_usu',
            },
        ),
    ]