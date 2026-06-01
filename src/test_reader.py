import os
from reader import EmailReader
from models import Email


def test_parse_english_headers():
    reader = EmailReader("inbox")
    subject, sender, body = reader.parse("Subject: Test\nFrom: a@b.com\n\nHello")
    assert subject == "Test"
    assert sender == "a@b.com"
    assert body == "Hello"

def test_parse_russian_headers():
    reader = EmailReader("inbox")
    subject, sender, body = reader.parse("Тема: Привет\nОт кого: ivan@mail.ru\n\nТело")
    assert subject == "Привет"
    assert sender == "ivan@mail.ru"
    assert body == "Тело"

def test_parse_translit_headers():
    reader = EmailReader("inbox")
    subject, sender, body = reader.parse("Tema: Privet\nOt kogo: test@test.ru\n\nTelo")
    assert subject == "Privet"
    assert sender == "test@test.ru"

def test_parse_no_headers():
    reader = EmailReader("inbox")
    subject, sender, body = reader.parse("Просто текст без заголовков")
    assert subject == ""
    assert sender == ""
    assert body == "Просто текст без заголовков"

def test_parse_empty_subject():
    reader = EmailReader("inbox")
    subject, sender, body = reader.parse("Subject: \n\nBody")
    assert subject == ""

def test_read_empty_file(tmp_path):
    path = os.path.join(str(tmp_path), "empty.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("")
    reader = EmailReader(str(tmp_path))
    email = reader.read_one("empty.txt")
    assert email.status == "broken"
    assert email.reason == "пустой файл"

def test_read_binary_file(tmp_path):
    path = os.path.join(str(tmp_path), "bad.bin")
    with open(path, "wb") as f:
        f.write(b"\xff\xfe\x00\x01")
    reader = EmailReader(str(tmp_path))
    email = reader.read_one("bad.bin")
    assert email.status == "broken"

def test_read_broken_json(tmp_path):
    path = os.path.join(str(tmp_path), "mail.json")
    with open(path, "w", encoding="utf-8") as f:
        f.write('{"subject": "Test", "body":')
    reader = EmailReader(str(tmp_path))
    email = reader.read_one("mail.json")
    assert email.status == "broken"
    assert email.reason == "повреждённый json"

def test_read_json(tmp_path):
    path = os.path.join(str(tmp_path), "mail.json")
    with open(path, "w", encoding="utf-8") as f:
        f.write('{"subject": "Test", "from": "a@b.com", "body": "Hello"}')
    reader = EmailReader(str(tmp_path))
    email = reader.read_one("mail.json")
    assert email.status == "ok"
    assert email.subject == "Test"
