from django.http import request
from rest_framework.permissions import BasePermission

class ClassroomPermissions(BasePermission):
  
  def has_permission(self, request, view):
    isProfessor = False
    try:
      if request.user.student:
        isProfessor = True
    except:
      isProfessor = False
    if request.method == ['GET'] and request.user.is_authenticated:
      return True
    if request.user.is_authenticated and isProfessor:
      return True
    return False