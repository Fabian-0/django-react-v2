from rest_framework.test import APITestCase
from django.contrib.auth.models import User
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

  # def setUp(self) -> None:

  #   # Create Professor and get token

  #   user = User.objects.create_user(username='user', password='password')
  #   response = self.client.post(f'{self.BASE_URL}/api/token/', data={'username': 'user', 'password': 'password'})
  #   Professor.objects.create(user=user)
  #   self.professor = user
  #   self.professor_token = response.data['access']


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
