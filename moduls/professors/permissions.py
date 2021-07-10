from rest_framework.permissions import BasePermission

class ProfessorPermissions(BasePermission):

  CUSTOM_SAVE_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE']

  def has_permission(self, request, view):
    print('-- BasePermissions Professors  --')
    isProfessor = False
    try:
      if request.user.student:
        isProfessor = True
    except:
      isProfessor = False
      
    method = request.method

    if method in self.CUSTOM_SAVE_METHODS and request.user.is_authenticated and isProfessor:
      return True

    if method == 'POST':
      return True

    return False

  def has_object_permission(self, request, view, obj):
    if not request.user.is_authenticated:
      return False
    print(request.user.is_authenticated, view.basename)
    return super().has_object_permission(request, view, obj)