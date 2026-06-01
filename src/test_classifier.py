from classifier import EmailClassifier
from models import Email

def test_spam():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Вы выиграли iPhone",
  body=""
  )
  assert classifier.classify(email) == "spam"

def test_critical_incident():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Критический инцидент",
  body="Production недоступен"
  )
  assert classifier.classify(email) == "critical_incidents"

def test_access_request():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Нужен доступ в Jira",
  body=""
  )
  assert classifier.classify(email) == "access_requests"

def test_hardware_issue():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Не работает принтер",
  body=""
  )
  assert classifier.classify(email) == "hardware_issues"

def test_software_issue():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Outlook не запускается",
  body=""
  )
  assert classifier.classify(email) == "software_issues"

def test_monitoring_alert():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Warning: CPU usage",
  body=""
  )
  assert classifier.classify(email) == "monitoring_alerts"

def test_documents_and_finance():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Договор на оплату",
  body=""
  )
  assert classifier.classify(email) == "documents_and_finance"

def test_hr_and_meetings():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Встреча по отпуску",
  body=""
  )
  assert classifier.classify(email) == "hr_and_meetings"

def test_other():
  classifier = EmailClassifier()
  email = Email(
  filename="mail.txt",
  subject="Добрый день",
  body="Просто письмо"
  )
  assert classifier.classify(email) == "other"

def test_unreadable():
  classifier = EmailClassifier()
  email = Email(
  filename="broken.txt",
  status="error"
  )
  assert classifier.classify(email) == "unreadable"



