import json
import matplotlib.pyplot as plt

def form_stats(name="stats.json"):
    with open(name,encoding="utf-8") as file:
        info = json.load(file)
    categories = {k: v for k,v in info.items() if k!="total"}
    return categories

def bar_chart(categories):
    plt.figure(figsize=(8,5))
    plt.bar(categories.keys(),categories.values(),color="navy")
    plt.title("Стобчатая диаграмма для иллюстрации количества писем по категориям")
    plt.xlabel("Категории")
    plt.ylabel("Количество")
    plt.savefig("bar_chart.png")
    plt.close()

def pie_chart(categories):
    plt.figure(figsize=(6,6))
    plt.pie(categories.values(),labels=categories.keys(),autopct="%1.1f%%")
    plt.title("Круговая диаграмма для иллюстрации распределения писем по категориям")
    plt.savefig("pie_chart.png")
    plt.close()

def main():
    categories = form_stats()
    bar_chart(categories)
    pie_chart(categories)
    

if __name__ == "__main__":
    main()