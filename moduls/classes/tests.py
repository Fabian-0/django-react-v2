from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from moduls.professors.models import Professor
from moduls.students.models import Student
from rest_framework.exceptions import NotAuthenticated


class ClassroomTestCase(APITestCase):
  
  BASE_URL = 'http://127.0.0.1:8000'

  def setUp(self) -> None:

    # Create Professor and get token

    user = User.objects.create_user(username='user', password='password')
    response = self.client.post(f'{self.BASE_URL}/api/token/', data={'username': 'user', 'password': 'password'})
    Professor.objects.create(user=user)
    self.professor = user
    self.professor_token = response.data['access']

    # Create Student and get token

    student = User.objects.create_user(username='student', password='password')
    studetn_response = self.client.post(f'{self.BASE_URL}/api/token/', data={'username': 'student', 'password': 'password'})
    Student.objects.create(user=user)
    self.student = student
    self.student_token = studetn_response.data['access']

  # Tests to Get

  def test_get_classes_without_token(self):
    response = self.client.get(f'{self.BASE_URL}/classes/')
    self.assertEqual(response.status_code, 401)
    self.assertRaises(NotAuthenticated)

  def test_get_classes_correctly(self):
    response = self.client.get(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}')

    self.assertAlmostEqual(response.status_code, 200)
    self.assertIsNotNone(response.data.get('results'))

  # Tests to Create

  def test_create_with_rol_not_supported(self):
    pass

  def test_create_class_without_data(self):
    response = self.client.post(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}')
    self.assertEqual(response.status_code, 400)
  
  def test_create_class_without_data_values(self):
    response = self.client.post(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', data = {})

    self.assertEqual(response.status_code, 400)

  def test_create_class_without_data_empty_name(self):
    response = self.client.post(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', data = {'name': ''})  
    self.assertEqual(response.status_code, 400)

  def test_create_class_correctly(self):
    response = self.client.post(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', data = {'name': 'test create'})  
    class_id = response.data.get('id')

    self.assertIsNotNone(class_id)
    self.assertEqual(response.status_code, 201)

  # Test to Update

  def test_update_inexistent_class(self):
    create_response = self.client.put(
      f'{self.BASE_URL}/classes/1A/', 
      HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', 
      data = {'name': '9'}
    )
    
    self.assertEqual(create_response.status_code, 404)

  def test_update_without_data(self):
    response = self.client.post(
      f'{self.BASE_URL}/classes/', 
      HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', 
      data = {'name': 'test update'}
    )  

    self.assertEqual(response.status_code, 201)

    class_id = response.data.get('id')
    
    self.assertIsNotNone(class_id)
    
    create_response = self.client.put(f'{self.BASE_URL}/classes/{class_id}/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}')
    
    self.assertEqual(create_response.status_code, 400)
  
  def test_update_with_empy_data(self):
    response = self.client.post(
      f'{self.BASE_URL}/classes/', 
      HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', 
      data = {'name': 'update'}
    ) 

    self.assertEqual(response.status_code, 201)
    
    class_id = response.data.get('id')
    
    self.assertIsNotNone(class_id)
    
    create_response = self.client.put(
      f'{self.BASE_URL}/classes/{class_id}/', 
      HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', 
      data ={'name': ''}
    )
    
    self.assertEqual(create_response.status_code, 400)

  def test_update_correctly(self):
    response = self.client.post(
      f'{self.BASE_URL}/classes/', 
      HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', 
      data = {'name': 'update'}
    ) 

    self.assertEqual(response.status_code, 201)
    
    class_id = response.data.get('id')
    
    self.assertIsNotNone(class_id)

    create_response = self.client.put(
      f'{self.BASE_URL}/classes/{class_id}/', 
      HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', 
      data ={'name': 'test update'}
    )
   
    self.assertEqual(create_response.status_code, 200)

  # Tests to Delete

  def test_delete_inexistent_class(self):
    response = self.client.delete(f'{self.BASE_URL}/classes/nan/', HTTP_AUTHORIZATION = f'Bearer {self.professor_token}')
  
    self.assertEqual(response.status_code, 404)

  def test_delete_class_not_owner(self):
    auth_response = self.client.post(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', data = {'name': 'test create'})  
    class_id = auth_response.data.get('id')

    self.assertIsNotNone(class_id)
    self.assertEqual(auth_response.status_code, 201)

    User.objects.create_user(username='user_test_delete', password='password')
    userResponse = self.client.post(f'{self.BASE_URL}/api/token/', data={'username': 'user_test_delete', 'password': 'password'})

    self.assertEqual(userResponse.status_code, 200)

    token = userResponse.data.get('access')

    self.assertIsNotNone(token)

    response = self.client.delete(f'{self.BASE_URL}/classes/{class_id}/', HTTP_AUTHORIZATION = f'Bearer {token}')
  
    self.assertEqual(response.status_code, 403)

  def test_delete_class_correctly(self): 
    response = self.client.post(f'{self.BASE_URL}/classes/', HTTP_AUTHORIZATION=f'Bearer {self.professor_token}', data = {'name': 'test create'})  
    class_id = response.data.get('id')

    self.assertIsNotNone(class_id)
    self.assertEqual(response.status_code, 201)   

    delete_response = self.client.delete(f'{self.BASE_URL}/classes/{class_id}/', HTTP_AUTHORIZATION = f'Bearer {self.professor_token}')
  
    self.assertEqual(delete_response.status_code, 204)