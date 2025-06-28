from django.contrib import admin
from .models import Staff, Intern, Manager, Address  # Import all models

# Register all models to appear in Django admin
admin.site.register(Staff)
admin.site.register(Intern)
admin.site.register(Manager)
admin.site.register(Address)
