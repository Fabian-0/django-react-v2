from rest_framework.permissions import BasePermission

class StuentPermissions(BasePermission):

  CUSTOM_SAFE_METHODS = ['GET','POST', 'PUT', 'PATCH', 'DELETE']
  
  def has_permission(self, request, view):

    isStudent = False
    try:
      if request.user.student:
        isStudent = True
    except:
      isStudent = False

    method = request.method
    if method == 'POST':
      return True
    if method in self.CUSTOM_SAFE_METHODS and request.user.is_authenticated and isStudent:
      return True
    return False
  
  def has_object_permission(self, request, view, obj):

    if request.user.id == obj.id:
      return True
    
    return False