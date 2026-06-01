from reader import EmailReader
from logger import MailLogger
from moveToFolder import MoveToFolder
from classifier import EmailClassifier
from visualization import form_stats, bar_chart, pie_chart, generate_html_report
import webbrowser
import os



def main():
    print("="*60)
    print("АВТОМАТИЗИРОВАННАЯ СИСТЕМА ОБРАБОТКИ КОРПОРАТИВНОЙ ПОЧТЫ")
    print("="*60)
    print("НАЧАЛО РАБОТЫ ПРОГРАММЫ")
    print("="*60)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    INBOX_DIR = os.path.join(BASE_DIR, '..', 'inbox')
    TEMPLATE_PATH = os.path.join(BASE_DIR, '..', 'template.html')
    reader = EmailReader(INBOX_DIR)
    mail = reader.read_all()
    print(f"НАЙДЕНО ПИСЕМ: {len(mail)}")
    mail_classif = EmailClassifier()
    for x in mail:
       x.category = mail_classif.classify(x)
    categories = []
    for x in mail:
      if x.category not in categories:
          categories.append(x.category)
    mail_fold = MoveToFolder("newfolders", categories)
    mail_fold.createFolder()
    mail_logg = MailLogger()
    for x in mail:
        mail_logg.log_email(x.filename, x.category)
        mail_fold.moveToFolder(x, INBOX_DIR, x.category)
        print(f"{x.filename} в категории {x.category}" )
    mail_logg.save_logs()
    mail_logg.save_stats()
    
    try:
        categories, total_emails = form_stats("stats.json")
        
        bar_chart(categories)
        pie_chart(categories)
        generate_html_report(categories, total_emails, TEMPLATE_PATH, report_name="report.html")
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
