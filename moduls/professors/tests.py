from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from moduls.students.models import Student
# Create your tests here.

class ProfessorTestCase(APITestCase):

  BASE_URL = 'http://127.0.0.1:8000'

  PROFESSOR_TEST_DATA = {
    "username": 'professor',
    "first_name": 'test',
    "last_name": 'test',
    "email": 'test@test.com',
    "password": 'password',
    "professor": {
    "phone_number": 9999999999,
    "avatar": 'https://test.com/',
    "gender": "male",
    "qualification": 'test'
    } 
  }
    
  # Create Tests

  def test_create_professor_without_data(self):

    response = self.client.post(f'{self.BASE_URL}/professor/')

    self.assertEqual(response.status_code, 400)

  def test_create_professor_with_empty_data(self):

    response = self.client.post(f'{self.BASE_URL}/professor/', data={})

    self.assertEqual(response.status_code, 400)

  def test_create_professor_with_partialt_data(self):

    response = self.client.post(f'{self.BASE_URL}/professor/', 
      data= {"username": 'professor',
        "first_name": 'test',
        "last_name": 'test',
        "email": 'test@test.com',
        "password": 'password', 
      }
    )

    self.assertEqual(response.status_code, 400)

  def test_create_correctly(self):

    response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')

    self.assertEqual(response.status_code, 201)

  # Get Tests

  def test_get_without_token(self):

    response = self.client.get(f'{self.BASE_URL}/professor/')

    self.assertEqual(response.status_code, 401)

  def test_get_with_wrong_rol(self):
    user = User.objects.create_user(username='student', password='password')
    Student.objects.create(user=user)

    response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={'username': 'student', 'password': 'password'}, 
    )

    token = response.data.get('access')

    self.assertEqual(response.status_code, 200)
    self.assertIsNotNone(token)

    auth_response = response = self.client.get(f'{self.BASE_URL}/professor/', HTTT_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(auth_response.status_code, 401)

  def test_get_correctly(self):

    create_response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')

    self.assertEqual(create_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.PROFESSOR_TEST_DATA['username'], 
        'password': self.PROFESSOR_TEST_DATA['password']
      } 
    )

    token = auth_response.data.get('access')

    self.assertEqual(auth_response.status_code, 200)
    self.assertIsNotNone(token)

    get_response = self.client.get(f'{self.BASE_URL}/professor/', HTTP_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(get_response.status_code, 200)

  #  Update Tests

  def test_update_wrong_rol(self):

    user = User.objects.create_user(username='student', password='password')
    Student.objects.create(user=user)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={'username': 'student', 'password': 'password'}, 
    )

    token = auth_response.data.get('access')

    self.assertEqual(auth_response.status_code, 200)
    self.assertIsNotNone(token)

    register_response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')
    professor_id = register_response.data.get('id')

    self.assertIsNotNone(professor_id)
    self.assertEqual(register_response.status_code, 201)
    

    update_response = self.client.patch(f'{self.BASE_URL}/professor/{professor_id}/', data={'username': 'test'}, HTTP_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(update_response.status_code, 403)

  def test_update_inexistent_professor(self):
    register_response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')
    professor_id = register_response.data.get('id')

    self.assertIsNotNone(professor_id)
    self.assertEqual(register_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.PROFESSOR_TEST_DATA['username'], 
        'password': self.PROFESSOR_TEST_DATA['password']
      } 
    )

    token = auth_response.data.get('access')

    self.assertEqual(auth_response.status_code, 200)
    self.assertIsNotNone(token)
    

    update_response = self.client.patch(f'{self.BASE_URL}/professor/test/', data={'username': 'test'}, HTTP_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(update_response.status_code, 404)

  def test_update_not_owner(self):
    register_response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')
    professor_id = register_response.data.get('id')

    self.assertIsNotNone(professor_id)
    self.assertEqual(register_response.status_code, 201)

    register_response_two = self.client.post(
      f'{self.BASE_URL}/professor/', 
      data={
        "username": 'professor_two',
        "first_name": 'test',
        "last_name": 'test',
        "email": 'test@test.com',
        "password": 'password',
        "professor": {
        "phone_number": 9999999999,
        "avatar": 'https://test.com/',
        "gender": "male",
        "qualification": 'test'
        } 
      }, 
      format='json'
    )
    professor_id_two = register_response_two.data.get('id')

    self.assertIsNotNone(professor_id_two)
    self.assertEqual(register_response_two.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': 'professor_two', 
        'password': self.PROFESSOR_TEST_DATA['password']
      } 
    )

    token = auth_response.data.get('access')

    self.assertEqual(auth_response.status_code, 200)
    self.assertIsNotNone(token)
    

    update_response = self.client.patch(f'{self.BASE_URL}/professor/{professor_id}/', data={'username': 'test'}, HTTP_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(update_response.status_code, 403)
  
  def test_update_correctly(self):
    register_response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')
    professor_id = register_response.data.get('id')

    self.assertIsNotNone(professor_id)
    self.assertEqual(register_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.PROFESSOR_TEST_DATA['username'], 
        'password': self.PROFESSOR_TEST_DATA['password']
      } 
    )

    token = auth_response.data.get('access')

    self.assertEqual(auth_response.status_code, 200)
    self.assertIsNotNone(token)
    

    update_response = self.client.patch(
      f'{self.BASE_URL}/professor/{professor_id}/', 
      data={'professor': 'testupdate'}, 
      HTTP_AUTHORIZATION=f'Bearer {token}',
    )

    self.assertEqual(update_response.status_code, 200)

  # Delete Tests

  def test_delete_without_token(self):
    delete_response = self.client.delete(
      f'{self.BASE_URL}/professor/test/', 
    )

    self.assertEqual(delete_response.status_code, 401)

  def test_delete_correctly(self):
    register_response = self.client.post(f'{self.BASE_URL}/professor/', data=self.PROFESSOR_TEST_DATA, format='json')
    professor_id = register_response.data.get('id')

    self.assertIsNotNone(professor_id)
    self.assertEqual(register_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.PROFESSOR_TEST_DATA['username'], 
        'password': self.PROFESSOR_TEST_DATA['password']
      } 
    )

    token = auth_response.data.get('access')

    self.assertEqual(auth_response.status_code, 200)
    self.assertIsNotNone(token)
    

    delete_response = self.client.delete(
      f'{self.BASE_URL}/professor/{professor_id}/',
      HTTP_AUTHORIZATION=f'Bearer {token}',
    )

    self.assertEqual(delete_response.status_code, 204)