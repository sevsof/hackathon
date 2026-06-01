KEYWORDS = {
    "spam": [
        "вы выиграли",
        "iphone",
        "приз",
        "подарок",
        "бонус",
        "акция",
        "скидка",
        "limited offer",
        "exclusive offer",
        "срочная верификация",
        "подтвердите пароль",
        "перейдите по ссылке"],

    "critical_incidents": [
        "critical",
        "критический",
        "массовый сбой",
        "авария",
        "недоступен",
        "недоступна",
        "упал",
        "упала",
        "не работает",
        "production",
        "prod",
        "ошибка 500",
        "срочно",
        "инцидент"],

    "access_requests": [
        "доступ",
        "права",
        "vpn",
        "gitlab",
        "confluence",
        "jira",
        "1c",
        "1с",
        "почта",
        "учетная запись",
        "учётная запись",
        "аккаунт",
        "новый сотрудник",
        "восстановить доступ"],

    "hardware_issues": [
        "принтер",
        "сканер",
        "ноутбук",
        "компьютер",
        "монитор",
        "мышь",
        "клавиатура",
        "гарнитура",
        "зарядка",
        "не включается",
        "не печатает"],

    "software_issues": [
        "outlook",
        "excel",
        "word",
        "антивирус",
        "приложение",
        "программа",
        "не запускается",
        "ошибка приложения",
        "обновление",
        "браузер"],

    "monitoring_alerts": [
        "warning",
        "info",
        "alert",
        "monitoring",
        "grafana",
        "healthcheck",
        "disk usage",
        "cpu usage",
        "memory usage",
        "метрика",
        "сервер"],

    "documents_and_finance": [
        "договор",
        "счет",
        "счёт",
        "акт",
        "оплата",
        "платеж",
        "платёж",
        "закрывающие документы",
        "накладная",
        "инвойс",
        "invoice"],

    "hr_and_meetings": [
        "встреча",
        "собеседование",
        "hr",
        "отпуск",
        "больничный",
        "созвон",
        "митинг",
        "совещание",
        "календарь"],
}

CATEGORY_ORDER = [
    "spam",
    "critical_incidents",
    "access_requests",
    "hardware_issues",
    "software_issues",
    "monitoring_alerts",
    "documents_and_finance",
    "hr_and_meetings",
]

def classify_email(email):
    if email.status != "ok":
        return "unreadable"
    text = f"{email.subject} {email.body}".lower()
    for category in CATEGORY_ORDER:
        for keyword in KEYWORDS[category]:
            if keyword in text:
                return category
    return "other"
