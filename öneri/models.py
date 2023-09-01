# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advert(models.Model):
    updatedate = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    companyid = models.ForeignKey('Company', models.DO_NOTHING, db_column='companyid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advert'


class Application(models.Model):
    date = models.DateField()
    content = models.TextField(blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    advertid = models.ForeignKey(Advert, models.DO_NOTHING, db_column='advertid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Company(models.Model):
    name = models.TextField()
    content = models.TextField(blank=True, null=True)
    category = models.TextField()
    type = models.BooleanField()
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DdAdvert(models.Model):
    update_date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.BinaryField()
    location = models.TextField()
    category = models.TextField()
    company = models.ForeignKey('DdCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dd_advert'


class DdApplication(models.Model):
    date = models.DateField()
    content = models.TextField()
    file = models.BinaryField()
    advert = models.ForeignKey(DdAdvert, models.DO_NOTHING)
    user = models.ForeignKey('DdUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dd_application'


class DdCompany(models.Model):
    name = models.TextField()
    content = models.TextField()
    category = models.TextField()
    type = models.BooleanField()
    user = models.ForeignKey('DdUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dd_company'


class DdResume(models.Model):
    category = models.TextField()
    phone = models.TextField()
    image = models.BinaryField()
    country = models.TextField()
    city = models.TextField()
    address = models.TextField()
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.TextField()
    department = models.TextField()
    description = models.TextField()
    user = models.ForeignKey('DdUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dd_resume'


class DdUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()
    role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dd_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Projects(models.Model):
    title = models.TextField()
    content = models.TextField(blank=True, null=True)
    thumbnail = models.BinaryField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    githublink = models.TextField(blank=True, null=True)
    videolink = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class Resume(models.Model):
    category = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gpa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resume'


class User(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    password = models.TextField()
    #role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class neriAdvert(models.Model):
    update_date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.BinaryField()
    location = models.TextField()
    category = models.TextField()
    advertcategory = models.TextField()
    company = models.ForeignKey('neriCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'öneri_advert'


class neriApplication(models.Model):
    date = models.DateField()
    content = models.TextField()
    file = models.BinaryField()
    advert = models.ForeignKey(neriAdvert, models.DO_NOTHING)
    user = models.ForeignKey('neriUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'öneri_application'


class neriCompany(models.Model):
    name = models.TextField()
    content = models.TextField()
    category = models.TextField()
    type = models.BooleanField()
    user = models.ForeignKey('neriUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'öneri_company'


class neriResume(models.Model):
    category = models.TextField()
    phone = models.TextField()
    image = models.BinaryField()
    country = models.TextField()
    city = models.TextField()
    address = models.TextField()
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.TextField()
    department = models.TextField()
    description = models.TextField()
    user = models.ForeignKey('neriUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'öneri_resume'


class neriUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()
    role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'öneri_users'
