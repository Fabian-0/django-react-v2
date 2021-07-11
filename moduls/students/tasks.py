from backend.celery import app
from django.core.mail import send_mail

@app.task(name='student-created')
def student_send_mail(email):

  send_mail(
    subject='Se ha registrado Correctamente',
    message='Bienvenido a la plataforma!',
    from_email='test@gmail.com',
    recipient_list=[email],
    fail_silently=True
  )
