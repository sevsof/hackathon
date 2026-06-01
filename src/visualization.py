import json
import matplotlib.pyplot as plt
from string import Template


def form_stats(name="stats.json"):
    with open(name,encoding="utf-8") as file:
        info = json.load(file)
    categories = {k: v for k,v in info.items() if k!="total"}
    total_emails = info.get("total", sum(categories.values()))
    return categories, total_emails

def bar_chart(categories):
    plt.figure(figsize=(8,5))
    plt.bar(categories.keys(),categories.values(),color="navy")
    plt.title("Столбчатая диаграмма для иллюстрации количества писем по категориям", fontsize=12)
    plt.xlabel("Категории")
    plt.ylabel("Количество")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  
    plt.savefig("bar_chart.png")
    plt.close()

def pie_chart(categories):
    plt.figure(figsize=(10,6))
    wedges, texts, autotexts = plt.pie(categories.values(),autopct="%1.1f%%")
    plt.legend(wedges, categories.keys(), title="Категории", loc="center left", bbox_to_anchor=(1, 0.5))
    plt.title("Круговая диаграмма для иллюстрации распределения писем по категориям", fontsize=12)
    plt.tight_layout()  
    plt.savefig("pie_chart.png", bbox_inches="tight")
    plt.close()
    
    
def generate_html_report(categories, total_emails, template_name="template.html", report_name="report.html"):
    table_rows = ""
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        table_rows += f"<tr><td>{category}</td><td>{count}</td></tr>\n"

    with open(template_name, "r", encoding="utf-8") as file:
        template_content = file.read()


    template = Template(template_content)
    final_html = template.substitute(
        total_emails=total_emails,
        table_rows=table_rows
    )


    with open(report_name, "w", encoding="utf-8") as file:
        file.write(final_html)
    
    print(f"Отчет успешно сгенерирован: {report_name}")

def main():
    categories, total_emails = form_stats()
    bar_chart(categories)
    pie_chart(categories)
    generate_html_report(categories, total_emails)
    

if __name__ == "__main__":
    main()