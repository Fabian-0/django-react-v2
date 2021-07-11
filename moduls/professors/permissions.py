from rest_framework.permissions import BasePermission

class ProfessorPermissions(BasePermission):

  CUSTOM_SAVE_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE']

  def has_permission(self, request, view):
    isProfessor = False
    try:
      if request.user.professor:
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
    if request.user.id == obj.id:
      return True
    return False