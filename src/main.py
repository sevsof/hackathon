from reader import EmailReader
from logger import MailLogger
from moveToFolder import MoveToFolder
from classifier import Classifier
from visualization import form_stats, bar_chart, pie_chart, generate_html_report
import webbrowser
import os

def main():
    print("="*60)
    print("АВТОМАТИЗИРОВАННАЯ СИСТЕМА ОБРАБОТКИ КОРПОРАТИВНОЙ ПОЧТЫ")
    print("="*60)
    print("НАЧАЛО РАБОТЫ ПРОГРАММЫ")
    print("="*60)
    reader = EmailReader('inbox')
    mail = reader.read_all()
    print(f"НАЙДЕНО ПИСЕМ: {len(mail)}")
    categories = ["spam", "critical_incidents", "access_requests", "software_issues", "hardware_issues", "monitorung_alerts", "documents_and_finance", "hr_and_meetings"]
    mail_fold = MoveToFolder("newfolders", categories)
    mail_fold.createFolder()
    mail_logg = MailLogger()
    mail_classif = Classifier()
    categories = mail_classif.get_categories()
    for x in mail:
        categ = mail_classif.classify(x)
        mail_logg.log_email(x.filename, categ)
        mail_fold.moveToFolder(email, "inbox", category)
        print(f"{x.filename} в категории {categ}" )
    mail_logg.save_logs()
    mail_logg.save_stats()
    
    try:
        categories, total_emails = form_stats("stats.json")
        
        bar_chart(categories)
        pie_chart(categories)
        generate_html_report(categories, total_emails, template_name="template.html", report_name="report.html")
        file_path = f"file://{os.path.abspath('report.html')}"
        
        print("Открываю отчет в браузере...")
        webbrowser.open(file_path)
        
    except Exception as e:
        print(f"[Ошибка] Не удалось сгенерировать отчет: {e}")
    print("="*60)
    print('ПРОГРАММА УСПЕШНО ЗАВЕРШЕНА')
    print("="*60)
if __name__ == '__main__':
    main()
