# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove ` ` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
         
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
         
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
         
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
         
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
         
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
         
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Borrowequipment(models.Model):
    borrowid = models.AutoField(db_column='borrowID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    equipmentid = models.ForeignKey('Equipments', models.DO_NOTHING, db_column='equipmentID')  # Field name made lowercase.
    deliverydate = models.DateField(db_column='deliveryDate')  # Field name made lowercase.
    approxreturndate = models.DateField(db_column='approxReturnDate')  # Field name made lowercase.
    description = models.TextField()
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')

    class Meta:
         
        db_table = 'borrowequipment'


class Consumedetails(models.Model):
    consumeid = models.ForeignKey('Consumematerials', models.DO_NOTHING, db_column='consumeID')  # Field name made lowercase.
    materialid = models.ForeignKey('Materials', models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'consumedetails'


class Consumematerials(models.Model):
    consumeid = models.AutoField(db_column='consumeID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    datetimeconsumed = models.DateTimeField(db_column='datetimeConsumed')  # Field name made lowercase.

    class Meta:
         
        db_table = 'consumematerials'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
         
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
         
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
         
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
         
        db_table = 'django_session'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='employeeID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    birthday = models.DateField()
    address = models.CharField(max_length=45)
    contactnumber = models.IntegerField()
    employeetypeid = models.ForeignKey('Employeetype', models.DO_NOTHING, db_column='employeeTypeID')  # Field name made lowercase.

    class Meta:
         
        db_table = 'employees'


class Employeetype(models.Model):
    employeetypeid = models.AutoField(db_column='employeeTypeID', primary_key=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='employeeType', max_length=45)  # Field name made lowercase.

    class Meta:
         
        db_table = 'employeetype'


class Equipmentcategory(models.Model):
    equipmentcategoryid = models.AutoField(db_column='equipmentCategoryID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=45)

    class Meta:
         
        db_table = 'equipmentcategory'


class Equipments(models.Model):
    equipmentid = models.AutoField(db_column='equipmentID', primary_key=True)  # Field name made lowercase.
    equipmentcategoryid = models.ForeignKey(Equipmentcategory, models.DO_NOTHING, db_column='equipmentCategoryID')  # Field name made lowercase.
    equipmentstatus = models.ForeignKey('Equipmentstatus', models.DO_NOTHING, db_column='equipmentStatus')  # Field name made lowercase.
    equipmentname = models.CharField(db_column='equipmentName', max_length=45)  # Field name made lowercase.
    description = models.CharField(max_length=50)

    class Meta:
         
        db_table = 'equipments'


class Equipmentstatus(models.Model):
    equipmentstatus = models.AutoField(db_column='equipmentStatus', primary_key=True)  # Field name made lowercase.
    status = models.TextField()

    class Meta:
         
        db_table = 'equipmentstatus'


class Initialprojectinventory(models.Model):
    initialid = models.AutoField(db_column='initialID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.

    class Meta:
         
        db_table = 'initialprojectinventory'


class Initialprojectinventorydetails(models.Model):
    initialid = models.ForeignKey(Initialprojectinventory, models.DO_NOTHING, db_column='initialID')  # Field name made lowercase.
    materialid = models.ForeignKey('Materials', models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'initialprojectinventorydetails'


class Materials(models.Model):
    materialid = models.AutoField(db_column='materialID', primary_key=True)  # Field name made lowercase.
    materialname = models.CharField(db_column='materialName', max_length=150)  # Field name made lowercase.
    unit = models.CharField(max_length=45)

    class Meta:
         
        db_table = 'materials'


class Projectemployees(models.Model):
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeID')  # Field name made lowercase.

    class Meta:
         
        db_table = 'projectemployees'


class Projectinventory(models.Model):
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'projectinventory'


class Projects(models.Model):
    projectid = models.AutoField(db_column='projectID', primary_key=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=45)  # Field name made lowercase.
    projectlocation = models.CharField(db_column='projectLocation', max_length=60)  # Field name made lowercase.
    projecttypeid = models.ForeignKey('Projecttype', models.DO_NOTHING, db_column='projectTypeID')  # Field name made lowercase.
    userid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.

    class Meta:
         
        db_table = 'projects'


class Projecttype(models.Model):
    projecttypeid = models.AutoField(db_column='projectTypeID', primary_key=True)  # Field name made lowercase.
    projecttype = models.CharField(db_column='projectType', max_length=45)  # Field name made lowercase.

    class Meta:
         
        db_table = 'projecttype'


class Receivematerials(models.Model):
    receiveid = models.AutoField(db_column='receiveID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    sendid = models.ForeignKey('Sendmaterial', models.DO_NOTHING, db_column='sendID', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status', blank=True, null=True)
    date = models.DateField()

    class Meta:
         
        db_table = 'receivematerials'


class Requestequipment(models.Model):
    requestid = models.AutoField(db_column='requestID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusID')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipments, models.DO_NOTHING, db_column='equipmentID')  # Field name made lowercase.
    dateneeded = models.DateField(db_column='dateNeeded')  # Field name made lowercase.
    returndate = models.DateField(db_column='returnDate')  # Field name made lowercase.
    description = models.TextField()
    datetimerequested = models.DateTimeField(db_column='datetimeRequested')  # Field name made lowercase.

    class Meta:
         
        db_table = 'requestequipment'


class Requestmaterialdetails(models.Model):
    requestid = models.ForeignKey('Requestmaterials', models.DO_NOTHING, db_column='requestID')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'requestmaterialdetails'


class Requestmaterials(models.Model):
    requestid = models.AutoField(db_column='requestID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusID')  # Field name made lowercase.
    dateneeded = models.DateField(db_column='dateNeeded')  # Field name made lowercase.
    datetimerequested = models.DateTimeField(db_column='datetimeRequested')  # Field name made lowercase.

    class Meta:
         
        db_table = 'requestmaterials'


class Requestnewequipment(models.Model):
    requestid = models.AutoField(db_column='requestID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusID')  # Field name made lowercase.
    equipmentname = models.CharField(db_column='equipmentName', max_length=150)  # Field name made lowercase.
    description = models.TextField()
    datetimerequested = models.DateTimeField(db_column='datetimeRequested')  # Field name made lowercase.
    dateneeded = models.DateField(db_column='dateNeeded')  # Field name made lowercase.

    class Meta:
         
        db_table = 'requestnewequipment'


class Requestnewmaterialdetails(models.Model):
    requestid = models.ForeignKey('Requestnewmaterials', models.DO_NOTHING, db_column='requestID')  # Field name made lowercase.
    materialname = models.CharField(db_column='materialName', max_length=100)  # Field name made lowercase.
    unit = models.CharField(max_length=11)
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'requestnewmaterialdetails'


class Requestnewmaterials(models.Model):
    requestid = models.AutoField(db_column='requestID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusID')  # Field name made lowercase.
    datetimerequested = models.DateTimeField(db_column='datetimeRequested')  # Field name made lowercase.
    dateneeded = models.DateField(db_column='dateNeeded')  # Field name made lowercase.

    class Meta:
         
        db_table = 'requestnewmaterials'


class Requestquotation(models.Model):
    requestquotationid = models.AutoField(db_column='requestQuotationID', primary_key=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')
    date = models.DateField()

    class Meta:
         
        db_table = 'requestquotation'


class Requestquotationdetails(models.Model):
    requestquotationid = models.ForeignKey(Requestquotation, models.DO_NOTHING, db_column='requestQuotationID')  # Field name made lowercase.
    material = models.CharField(max_length=150)
    unit = models.CharField(max_length=45)
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'requestquotationdetails'


class Requestquotationeqpt(models.Model):
    requestquotationeqptid = models.AutoField(db_column='requestQuotationeqptID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusID')  # Field name made lowercase.
    equipmentname = models.CharField(db_column='equipmentName', max_length=150)  # Field name made lowercase.
    dateneeded = models.DateField(db_column='dateNeeded')  # Field name made lowercase.

    class Meta:
         
        db_table = 'requestquotationeqpt'


class Returnequipment(models.Model):
    returnid = models.AutoField(db_column='returnID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipments, models.DO_NOTHING, db_column='equipmentID')  # Field name made lowercase.
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')
    returndate = models.DateField(db_column='returnDate')  # Field name made lowercase.

    class Meta:
         
        db_table = 'returnequipment'


class Returnmaterial(models.Model):
    returnid = models.AutoField(db_column='returnID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID')  # Field name made lowercase.
    date = models.DateField()

    class Meta:
         
        db_table = 'returnmaterial'


class Returnmaterialdetails(models.Model):
    returnid = models.ForeignKey(Returnmaterial, models.DO_NOTHING, db_column='returnID')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'returnmaterialdetails'


class Sendmaterial(models.Model):
    sendid = models.AutoField(db_column='sendID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    sendto = models.ForeignKey(Employees, models.DO_NOTHING, db_column='sendTo')  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='projectID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField()
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')
    date = models.DateField()

    class Meta:
         
        db_table = 'sendmaterial'


class Sendmaterialdetails(models.Model):
    sendid = models.ForeignKey(Sendmaterial, models.DO_NOTHING, db_column='sendID')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'sendmaterialdetails'


class Spoilageaudit(models.Model):
    spoilageid = models.AutoField(db_column='spoilageID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    reason = models.TextField()
    date = models.DateField()

    class Meta:
         
        db_table = 'spoilageaudit'


class Spoilagedetails(models.Model):
    spoilageid = models.ForeignKey(Spoilageaudit, models.DO_NOTHING, db_column='spoilageID')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='materialID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'spoilagedetails'


class Spoilageequipment(models.Model):
    spoilageid = models.OneToOneField(Spoilageaudit, models.DO_NOTHING, db_column='spoilageID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipments, models.DO_NOTHING, db_column='equipmentID')  # Field name made lowercase.

    class Meta:
         
        db_table = 'spoilageequipment'


class Status(models.Model):
    statusid = models.AutoField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=50)

    class Meta:
         
        db_table = 'status'


class Users(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeID')  # Field name made lowercase.

    class Meta:
         
        db_table = 'users'


class Warehouseinventory(models.Model):
    materialid = models.OneToOneField(Materials, models.DO_NOTHING, db_column='materialID', unique=True)  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
         
        db_table = 'warehouseinventory'
