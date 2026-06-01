from reader import EmailReader
from logger import MailLogger
from moveToFolder import MoveToFolder
from classifier import Classifier
def main():
    print("="*60)
    print("АВТОМАТИЗИРОВАННАЯ СИСТЕМА ОБРАБОТКИ КОРПОРАТИВНОЙ ПОЧТЫ")
    print("="*60)
    print("НАЧАЛО РАБОТЫ ПРОГРАММЫ")
    print("="*60)
    reader = EmailReader('inbox')
    mail = reader.read_all()
    print(f"НАЙДЕНО ПИСЕМ: {len(mail)}")
    categories = [] //дописать
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
    print("="*60)
    print('ПРОГРАММА УСПЕШНО ЗАВЕРШЕНА')
    print("="*60)
if __name__ == '__main__':
    main()
