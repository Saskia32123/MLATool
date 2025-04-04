# Create your models here.
import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

''' 
This class defines the WorkPackage model, which are also the main components of the dashboard. Basically all other 
models are dependent on this one.
'''
class WorkPackage(models.Model):
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """
        Was this entry published recently?

        Returns True if the entry's publication date is less than or
        equal to seven days ago, and False otherwise.

        The `ordering` argument to the `@admin.display` decorator means
        that Django will use this method to determine the order of the
        "Published recently?" column in the admin interface.

        The `boolean` argument to the `@admin.display` decorator means
        that the result of this method will be formatted as a boolean
        value (True or False) when displayed in the admin interface.

        The `description` argument to the `admin.display` decorator means
        that the label for this column in the admin interface will be
        "Published recently?".
        """
        now = datetime.datetime.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

    WP_ID = models.CharField(max_length=150, default="-")

    # Per default those three rating categories are available (+ Undefined to represent a not yet decided rating)
    class Rating(models.TextChoices):
        Rot = "ROT"
        Gelb = "GELB"
        Gruen = "GRÜN"
        Undefined = "Undefined"

    # Per default those three rating categories are available (+ Undefined to represent a not yet decided rating)
    class Area(models.TextChoices):
        RG_A = "ML-A"
        RG_B = "ML-B"
        RG_C = "ML-C"
        RG_D = "ML-D"
        RG_E = "ML-E"
        RG_F = "ML-F"
        Undefined = "Undefined"

    class Groups(models.TextChoices):
        Vehicle_Security_Architect = "Vehicle Security Architect"
        CarIT_Carline_Coordinator = "CarIT Carline Coordinator"
        CarIT_Risk_Manager = "CarIT Risk Manager"
        Procurement_MP = "Procurement MP"
        CarIT_Supplier_Manager = "CarIT Supplier Manager"
        Security_Architect = "Security Architect"
        CarIT_Governance_Coordinator = "CarIT Governance Coordinator"
        E2 = "E2"
        PL_Carline = "PL Carline"
        Vehicle_Pentest_Coordinator = "Vehicle Pentest Coordinator"
        BTV = "BTV"
        CarIT_Security_Mandate = "CarIT Security Manadate"
        Supplier = "Supplier"
        Not_Defined = "N/A"

    rg_area = models.CharField(choices=Area, max_length=150, null=True)
    kpi = models.CharField(max_length=150)
    kpi_species = models.CharField(max_length=250)
    details = models.TextField()

    # The performer rates this workpackage
    performer = models.CharField(max_length=150)
    performer_rating = models.CharField(choices=Rating, max_length=50, null=True)

    # The recipient rates this workpackage, too
    # Recipient rating is also Total_Rating
    recipient = models.CharField(max_length=150)
    recipient_rating = models.CharField(choices=Rating, max_length=50, null=True)

    wp = models.TextField()
    link = models.URLField(null=True)
    file = models.FileField(upload_to='files/', null=True)
    archieving_relevance = models.BooleanField()

    pub_date = models.DateField("pub date", default=datetime.datetime.now)

    def __str__(self):
        return self.kpi


    def get_absolute_url(self):
        return reverse("WorkPackage:WorkPackage_detail", kwargs={"wp_id":self.WP_ID})


''' 
This class is just needed when the total_rating isn't green and steps need to be done before accepting this state, so 
it's optional and often "none" as no measures need to take place.
'''
class MeasuresForBadRating(models.Model):
    work_package = models.OneToOneField(WorkPackage, on_delete=models.CASCADE, null=True)
    problem_description_performer = models.CharField(default="None", max_length=200)
    problem_description_recipient = models.CharField(default="None", max_length=200)
    measure = models.CharField(default="None", max_length=200)
    votes = models.IntegerField(default=0)

    deadline = models.DateTimeField("date published", default=datetime.datetime.now())

    def __str__(self):
        return self.problem_description_performer


class TestPackage(models.Model):
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """
        Was this entry published recently?

        Returns True if the entry's publication date is less than or
        equal to seven days ago, and False otherwise.

        The `ordering` argument to the `@admin.display` decorator means
        that Django will use this method to determine the order of the
        "Published recently?" column in the admin interface.

        The `boolean` argument to the `@admin.display` decorator means
        that the result of this method will be formatted as a boolean
        value (True or False) when displayed in the admin interface.

        The `description` argument to the `admin.display` decorator means
        that the label for this column in the admin interface will be
        "Published recently?".
        """
        now = datetime.datetime.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

    WP_ID = models.CharField(max_length=150)
    #Per default those three rating categories are available (+ Undefined to represent a not yet decided rating)
    class Rating(models.TextChoices):
        Rot = "ROT"
        Gelb = "GELB"
        Gruen = "GRÜN"
        Undefined = "Undefined"

    # Per default those three rating categories are available (+ Undefined to represent a not yet decided rating)
    class Area(models.TextChoices):
        RG_A = "RG_A"
        RG_B = "RG_B"
        RG_C = "RG_C"
        RG_D = "RG_D"
        RG_E = "RG_E"
        RG_F = "RG_F"
        Undefined = "Undefined"
    rg_area = models.CharField(choices=Area, max_length=150, null=True)
    kpi = models.CharField(max_length=150)
    kpi_species = models.CharField(max_length=250)
    details = models.TextField()
    #The performer rates this workpackage
    performer = models.CharField(max_length=150)
    performer_rating = models.CharField(choices=Rating, max_length=50, null=True)

    #And also the recipient rates this workpackage
    recipient = models.CharField(max_length=150)
    recipient_rating = models.CharField(choices=Rating, max_length=50, null=True)

    #The recipient overrules the performer rating. No matter what the performer rates this work package
    total_rating = models.CharField(choices=Rating, max_length=50, null=True)

    wp = models.TextField()
    link = models.URLField(null=True)
    file = models.FileField(upload_to='files/', null=True)
    archieving_relevance = models.BooleanField()

    pub_date = models.DateField("pub date", default=datetime.datetime.now)

    readonly_fields=('kpi_species', 'details', 'rg_area', 'kpi', 'WP_ID', 'total_rating', 'wp', 'archieving_relevance', 'pub_date')


    def __str__(self):
        return self.kpi


