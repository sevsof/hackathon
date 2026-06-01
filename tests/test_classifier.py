from hackathon.src.classifier import classify_email
from hackathon.src.models import Email

def test_spam():
  email = Email(
  filename="mail.txt",
  subject="Вы выиграли iPhone",
  body=""
  )
  assert classify_email(email) == "spam"

def test_critical_incident():
  email = Email(
  filename="mail.txt",
  subject="Критический инцидент",
  body="Production недоступен"
  )
  assert classify_email(email) == "critical_incidents"

def test_access_request():
  email = Email(
  filename="mail.txt",
  subject="Нужен доступ в Jira",
  body=""
  )
  assert classify_email(email) == "access_requests"

def test_hardware_issue():
  email = Email(
  filename="mail.txt",
  subject="Не работает принтер",
  body=""
  )
  assert classify_email(email) == "hardware_issues"

def test_software_issue():
  email = Email(
  filename="mail.txt",
  subject="Outlook не запускается",
  body=""
  )
  assert classify_email(email) == "software_issues"

def test_monitoring_alert():
  email = Email(
  filename="mail.txt",
  subject="Warning: CPU usage",
  body=""
  )
  assert classify_email(email) == "monitoring_alerts"

def test_documents_and_finance():
  email = Email(
  filename="mail.txt",
  subject="Договор на оплату",
  body=""
  )
  assert classify_email(email) == "documents_and_finance"

def test_hr_and_meetings():
  email = Email(
  filename="mail.txt",
  subject="Встреча по отпуску",
  body=""
  )
  assert classify_email(email) == "hr_and_meetings"

def test_other():
  email = Email(
  filename="mail.txt",
  subject="Добрый день",
  body="Просто письмо"
  )
  assert classify_email(email) == "other"

def test_unreadable():
  email = Email(
  filename="broken.txt",
  status="error"
  )
  assert classify_email(email) == "unreadable"



