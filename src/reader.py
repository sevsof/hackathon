import os
import json
from models import Email


class EmailReader:
    SUBJECT_PREFIXES = ("Subject:", "Тема:", "Tema:")
    SENDER_PREFIXES = ("From:", "От кого:", "Отправитель:", "Ot kogo:", "Otpravitel:")
    HEADER_PREFIXES = ("Subject:", "From:", "To:", "Date:",
                       "Тема:", "От кого:", "Кому:", "Дата:",
                       "Tema:", "Ot kogo:", "Komu:", "Data:")

    def __init__(self, inbox_path):
        self.inbox_path = inbox_path
        self.log = [] 

    def read_all(self):
        emails = []
        for filename in sorted(os.listdir(self.inbox_path)):
            full_path = os.path.join(self.inbox_path, filename)
            if not os.path.isfile(full_path):
                continue
            if filename.startswith("."):
                self.note(filename, "пропущен системный файл")
                continue

            emails.append(self.read_one(filename))
        return emails

    def read_one(self, filename):
        full_path = os.path.join(self.inbox_path, filename)
        try:
            with open(full_path, encoding="utf-8") as file:
                text = file.read()
        except UnicodeDecodeError:
            self.note(filename, "не текстовый файл, не читается как письмо")
            return Email(filename, status="broken", reason="бинарный/нечитаемый файл")
        except OSError as error:
            self.note(filename, f"ошибка открытия: {error}")
            return Email(filename, status="broken", reason="файл не открылся")

        if text.strip() == "":
            self.note(filename, "пустой файл")
            return Email(filename, status="broken", reason="пустой файл")

        if filename.endswith(".json"):
            return self.parse_json(filename, text)

        subject, sender, body = self.parse(text)
        return Email(filename, subject, sender, body)

    def parse_json(self, filename, text):
        try:
            data = json.loads(text)
        except ValueError:
            self.note(filename, "повреждённый json")
            return Email(filename, status="broken", reason="повреждённый json")
        return Email(
            filename,
            subject=data.get("subject", ""),
            sender=data.get("from", ""),
            body=data.get("body", ""),
        )

    def parse(self, text):
        header_part, body = "", text
        if "\n\n" in text:
            head, rest = text.split("\n\n", 1)
            looks_like_headers = any(
                line.startswith(self.HEADER_PREFIXES)
                for line in head.split("\n")
            )
            if looks_like_headers:
                header_part, body = head, rest

        subject = ""
        sender = ""
        for line in header_part.split("\n"):
            value = self.value_after(line, self.SUBJECT_PREFIXES)
            if value is not None:
                subject = value
                continue
            value = self.value_after(line, self.SENDER_PREFIXES)
            if value is not None:
                sender = value

        return subject, sender, body.strip()

    def value_after(self, line, prefixes):
        for prefix in prefixes:
            if line.startswith(prefix):
                return line[len(prefix):].strip()
        return None

    def note(self, filename, message):
        self.log.append(f"[{filename}] {message}")