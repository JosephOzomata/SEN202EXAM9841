from django.db import models

# Base Staff model
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def get_info(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

# Intern inherits from Staff
class Intern(Staff):
    school = models.CharField(max_length=100)
    duration_months = models.IntegerField()

    def __str__(self):
        return f"Intern: {self.first_name} {self.last_name}"

# Manager inherits from Staff
class Manager(Staff):
    department = models.CharField(max_length=100)
    num_team_members = models.IntegerField()

    def __str__(self):
        return f"Manager: {self.first_name} {self.last_name}"

# Address is linked to Staff
class Address(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
