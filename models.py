from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_name}{self.store_address}"


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    serial = models.CharField(max_length=100, null=True)
    # datetime = models.DateTimeField(auto_now=True)
    details = models.TextField(max_length=200, null=True)
    brand = models.CharField(max_length=100, null=True)
    # image
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=50, null=True)
    CATEGORIE_TYPE = (
        ('ELECTRONIC', 'Electronic'),  # 'sonic'),
        ('OFFICE', 'offce'),
        ("COMPUTER", "computer"),  # "dell","hp","acer","toshiba","MacBook"),
        ("PRINTER", "Printer"),  # "hp","epison")
        ("Food", "Food"),
    )
    categorie = models.CharField(max_length=255, choices=CATEGORIE_TYPE, null=True)
    BRAND_TYPE = (

        ("lenovo", "IdeaPad"),  # ,"Legion","ThinkPad","ThinkBook","Yoga"),
        ('HP', "EliteBook"),  # ,"Envy","Omen","Pavilion","ZBook","Spectre","Victus","ProBook","OmniBook"),
        ('Dell', "Alienware"),  # "G-Series","Inspiron","Latitude","Precision","Vostro","XPS"),
        ('Apple', "MacBook"),  # "MacBook Air","MacBook Pro"),
        ('Asus', "Zenbook"),
        # "Vivobook","Chromebook","ROG","TUF","ZEPHYRUS","EeeBook","Expertbook","Transformer","ASUSPRO","ProArt"),
    )
    brand = models.CharField(max_length=255, choices=BRAND_TYPE, null=True)
    CONDITION_TYPE = (
        ('NEW', 'New'),
        ('USED', 'Used')
    )
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE, null=True)
    STATUS_TYPES = (
        ('AVAILABLE', 'Available'),
        ('NOT AVAILABLE', 'Not Available'),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES, null=True)

    # operation = new
    def __str__(self):
        return f"{self.name},{self.brand},{self.status},{self.serial},{self.quantity},{self.categorie},{self.condition}"


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_address = models.CharField(max_length=100)

    # relation between store and department
    # store_id = db.Column(db.Integer,db.ForeignKey("store_table.id"))
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.department_name}{self.department_address}"


# 2 staff
class Staff(models.Model):
    staff_department = models.CharField(max_length=100)
    staff_first_name = models.CharField(max_length=100)
    staff_last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # relationship between users and store
    # store_id = db.Column(db.Integer, db.ForeignKey("store_table.id"))
    staff_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.staff_department}{self.staff_first_name}{self.staff_last_name}{self.username}"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('RECEIVE', 'Receive'),
        ('ISSUE', 'Issue'),
    )
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey('Staff', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.item.name} - {self.date}"
