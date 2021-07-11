from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from moduls.professors.models import Professor
from moduls.classes.models import Classroom

# Create your tests here.

class StudentTestCase(APITestCase):

  BASE_URL = 'http://127.0.0.1:8000'
  
  STUDENT_TEST_DATA = {
    "username": 'student',
    "first_name": 'test',
    "last_name": 'test',
    "email": 'test@test.com',
    "password": 'password',
    "student": {
    "phone_number": 9999999999,
    "avatar": 'https://test.com/',
    "gender": "male"
    } 
  }
  
  STUDENT_TWO_TEST_DATA = {
    "username": 'studentTwo',
    "first_name": 'test',
    "last_name": 'test',
    "email": 'test@test.com',
    "password": 'password',
    "student": {
    "phone_number": 9999999999,
    "avatar": 'https://test.com/',
    "gender": "female"
    } 
  }
  
  def test_create_empty(self):
    response = self.client.post(f'{self.BASE_URL}/student/')

    self.assertEqual(response.status_code, 400)

  def test_create_with_partial_data(self):
    response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data={"username": 'professor',
      "first_name": 'test',
      "last_name": 'test',
      "email": 'test@test.com',
      "password": 'password',
      }
    )

    self.assertEqual(response.status_code, 400)

  def test_create_correctly(self):

    response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(response.status_code, 201)

    # Get Tests

  def test_get_without_token(self):
    
    response = self.client.post(f'{self.BASE_URL}/student/')

    self.assertEqual(response.status_code, 400)    

  def test_get_wrong_rol(self):
    user = User.objects.create_user(username='Professor', password='password')
    Professor.objects.create(user=user)

    response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={'username': 'Professor', 'password': 'password'},
    )    

    token = response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(response.status_code, 200)

    get_response = self.client.get(f'{self.BASE_URL}/student/', HTTP_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(get_response.status_code , 403)

  def test_get_correctly(self):
    create_response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = create_response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.STUDENT_TEST_DATA['username'], 
        'password': self.STUDENT_TEST_DATA['password']
      }
    )    

    token = auth_response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(auth_response.status_code, 200)

    get_response = self.client.get(f'{self.BASE_URL}/student/', HTTP_AUTHORIZATION=f'Bearer {token}')

    self.assertEqual(get_response.status_code , 200)

    # Update Tests

  # Update Tests

  def test_update_correctly(self):
    create_response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = create_response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.STUDENT_TEST_DATA['username'], 
        'password': self.STUDENT_TEST_DATA['password']
      }
    )    

    token = auth_response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(auth_response.status_code, 200)

    update_response = self.client.patch(
      f'{self.BASE_URL}/student/{student_id}/',
      data= {
        'first_name': 'testupdate',
        'phone_number': 223333333
      }, 
      HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    self.assertEqual(update_response.status_code , 200)

  def test_update_wrong_user(self):
    create_response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = create_response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response.status_code, 201)

    create_response_two = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TWO_TEST_DATA,
      format='json'
    )

    student_two_id = create_response_two.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response_two.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.STUDENT_TEST_DATA['username'], 
        'password': self.STUDENT_TEST_DATA['password']
      }
    )    

    token = auth_response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(auth_response.status_code, 200)

    update_response = self.client.patch(
      f'{self.BASE_URL}/student/{student_two_id}/',
      data= {
        'first_name': 'testupdate',
        'phone_number': 223333333
      }, 
      HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    self.assertEqual(update_response.status_code , 403)

  # Delete Tests

  def test_delete(self):
    create_response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = create_response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.STUDENT_TEST_DATA['username'], 
        'password': self.STUDENT_TEST_DATA['password']
      }
    )    

    token = auth_response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(auth_response.status_code, 200)
  
    delete_response = self.client.delete(
      f'{self.BASE_URL}/student/{student_id}/', 
      HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    self.assertEqual(delete_response.status_code , 204)

    # Action 'classes' Post

  def test_post_action(self):
    user = User.objects.create_user(username = 'professorAction', password='password')
    Professor.objects.create(user=user)
    test_class = Classroom.objects.create(professor=user, name = 'testAction')

    create_response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = create_response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.STUDENT_TEST_DATA['username'], 
        'password': self.STUDENT_TEST_DATA['password']
      }
    )    

    token = auth_response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(auth_response.status_code, 200)
    
    add_class_response = self.client.post(
      f'{self.BASE_URL}/student/{student_id}/classes/', 
      data={'id': test_class.id},
      HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    self.assertEqual(add_class_response.status_code, 201)

  def test_delete_action(self):
    user = User.objects.create_user(username = 'professorAction', password='password')
    Professor.objects.create(user=user)
    test_class = Classroom.objects.create(professor=user, name = 'testAction')

    create_response = self.client.post(
      f'{self.BASE_URL}/student/', 
      data=self.STUDENT_TEST_DATA,
      format='json'
    )

    student_id = create_response.data.get('id')

    self.assertIsNotNone(student_id)
    self.assertEqual(create_response.status_code, 201)

    auth_response = self.client.post(
      f'{self.BASE_URL}/api/token/', 
      data={
        'username': self.STUDENT_TEST_DATA['username'], 
        'password': self.STUDENT_TEST_DATA['password']
      }
    )    

    token = auth_response.data.get('access')

    self.assertIsNotNone(token)
    self.assertEqual(auth_response.status_code, 200)
    
    add_class_response = self.client.post(
      f'{self.BASE_URL}/student/{student_id}/classes/', 
      data={'id': test_class.id},
      HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    self.assertEqual(add_class_response.status_code, 201)

    delete_class_response = self.client.delete(
      f'{self.BASE_URL}/student/{test_class.id}/classes/', 
      HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    self.assertEqual(delete_class_response.status_code, 200)