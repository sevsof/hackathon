from reader import EmailReader

def main():
    inbox_dir = "inbox" 
    
    print("Запуск системы обработки почты...")
    reader = EmailReader(inbox_dir)
    
    emails = reader.read_all()
    
    print(f"Успешно обработано файлов: {len(emails)}")
    for mail in emails:
        print(mail)
        
    if reader.log:
        print("\nЛог ошибок чтения:")
        for record in reader.log:
            print(record)

if __name__ == "__main__":
    main()