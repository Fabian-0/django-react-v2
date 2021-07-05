from rest_framework.permissions import BasePermission

methods = ['GET','POST', 'DELETE']
class StuentPermissions(BasePermission):

  def has_permission(self, request, view):
    print(request.user.is_authenticated)
    method = request.method
    if method == 'POST':
      return True
    if method in methods and request.user.is_authenticated:
      print('test')
      return True
    return False