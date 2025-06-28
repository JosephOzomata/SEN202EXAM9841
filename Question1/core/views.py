from django.http import JsonResponse
from .models import Staff

def staff_list(request):
    staffs = Staff.objects.all()
    data = [staff.get_info() for staff in staffs]  # encapsulation
    return JsonResponse(data, safe=False)
