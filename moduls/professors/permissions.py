from rest_framework.permissions import BasePermission

class ProfessorPermissions(BasePermission):

  def has_permission(self, request, view):
    print('-- BasePermissions Professors  --')
    method = request.method 
    if method == 'GET'  or method == 'PUT' or method == 'PATCH' and request.user.is_authenticated:
      return True

    if method == 'POST':
      return True

    if method == 'DELETE':
      return True
    
    return False

  def has_object_permission(self, request, view, obj):
    if not request.user.is_authenticated:
      return False
    print(request.user.is_authenticated, view.basename)
    return super().has_object_permission(request, view, obj)