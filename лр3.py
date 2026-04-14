"""""
import os
my = os.environ['SECRET_KEY']
print(my)

#Задание номер 1 (делала с Мурзагалиевой Эльмирой)
import os
GOSHKO = os.environ['GOSHKO']
print(GOSHKO)

import os
SECRET_KEY_GOSHKO = os.environ['SECRET_KEY_GOSHKO']
print(SECRET_KEY_GOSHKO)

import os
GOSHKO_KEY = os.environ['GOSHKO_KEY']
print(GOSHKO_KEY)

import os
SECRET_KEY = os.environ['SECRET_KEY']
print(SECRET_KEY)

#Задание номер 2 вариант 5 (Делала с Черепановым Майеславом)
#Контейнер расчета

from sympy import *
k, T, C, L = symbols('k C T L')

#пункт 1

C_ost = 20000 #Замена выполнена верно
Am_lst = []
C_ost_lst = []
for i in range(6):#Замена выполнена верно
  Am = (C - L)/T
  C_ost -= Am.subs({C: 20000, T:6, L:0}) #Замена выполнена верно
  Am_lst.append(round(Am.subs({C: 20000, T:6, L:0}), 2)) #Замена выполнена верно
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst) 
print('C_ost_lst:', C_ost_lst) 
#пункт 2

Aj = 0
C_ost = 20000 #Замена выполнена верно
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(6): #Замена выполнена верно
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 20000, T:6, k:2}) # Замена выполнена верно
  Am_lst_2.append(round(Am.subs({C: 20000, T:6, k:2}), 2)) #Замена выполнена верно
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am.lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Пункт 3
#Линейный способ

from sympy import *
k, T, C, L =symbols("k C T L")

C_ost = 20000   #Замена выполнена верно
Am_lst = []
C_ost_lst = []
for i in range(6):  #Замена выполнена верно
  Am = (C - L) / T
  C_ost -= Am.subs ({C:20000, T:6, L:0})  #Замена выполнена верно
  Am_lst.append(round(Am.subs({C: 20000, T:6, L:0}), 2))  #Замена выполнена верно
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#Способ уменьшаемого остатка 

Aj = 0 
C_ost = 20000  #Замена выполнена верно
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(6):  #Замена выполнена верно
   Am = k * 1 / T * (C - Aj)
   C_ost -= Am.subs({C: 20000, T:6, k:2})  #Замена выполнена верно
   Am_lst_2.append(round(Am.subs({C: 20000, T:6, k:2}), 2)) #Замена выполнена верно
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода 

import pandas as pd
Y = range(1, 7)  #Замена выполнена верно
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#Контейнер визуализатора 

import numpy as np 
import matplotlib.pyplot as plt 
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart8.png')


vals = Am_lst
labels = [str(x) for x in range(1,7)]    #Замена выполнена верно
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  #Замена выполнена верно
fig, ax = plt.subplots()
ax.pie(
  vals, 
  labels = labels, 
  autopct = '%1.1f%%', 
  shadow = True, 
  explode = explode, 
  wedgeprops = {'lw':1, 'ls':'--', 'edgecolor': 'k'},
  rotatelabels = True  
)
ax.axis("equal")
plt.savefig('chart9.png')

vals = Am_lst_2
labels = [str(x) for x in range (1,7)]  #Замена выполнена верно
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #Замена выполнена верно
fig, ax = plt.subplots()
ax.pie(
  vals,
  labels = labels,
  autopct = '%1.1f%%',
  shadow = True,
  explode = explode,
  wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': "k"},
  rotatelabels = True
)
ax.axis("equal")
plt.savefig('chart10.png')

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.png')
#Задание сделано правильно, 5 баллов, возьми с полки пирожок

#Задание 3 сделано


#Задание номер 4 (делала с Полиной Зайцевой)
#Контейнер расчета

from sympy import *
k, T, C, L = symbols('k C T L')

#пункт 1

C_ost = 100000
Am_lst = []
C_ost_lst = []
for i in range(5):
  Am = (C - L)/T
  C_ost -= Am.subs({C: 100000, T:5, L:0})
  Am_lst.append(round(Am.subs({C: 100000, T:5, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst) 
print('C_ost_lst:', C_ost_lst) 
#пункт 2

Aj = 0
C_ost = 100000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(5):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 100000, T:5, k:2})
  Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2)) #Что это значит? (Зайцева П.)
  #Ответ: это значит, что мы добавляем в список C_ost_lst_2 значение C_ost, округленное до 2 знаков после запятой (Гошко Я.)
  #Ответ правильный, 5 баллов (Зайцева П.)
print('Am.lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Пункт 3
#Линейный способ

from sympy import *
k, T, C, L =symbols("k C T L")

C_ost = 30000
Am_lst = []
C_ost_lst = []
for i in range(8):
  Am = (C - L) / T
  C_ost -= Am.subs ({C:30000, T:8, L:0})
  Am_lst.append(round(Am.subs({C: 30000, T:8, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#Способ уменьшаемого остатка 

Aj = 0 
C_ost = 30000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8):
   Am = k * 1 / T * (C - Aj)
   C_ost -= Am.subs({C: 30000, T:8, k:2})
   Am_lst_2.append(round(Am.subs({C: 30000, T:8, k:2}), 2))
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода 

import pandas as pd
Y = range(1, 9) #Что это значит? (Зайцева П.) 
#Ответ: это значит, что мы создаем переменную Y, которая будет принимать значения от 1 до 8 (Гошко Я.)
#Ответ правильный, 5 баллов (Зайцева П.)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#Контейнер визуализатора 

import numpy as np 
import matplotlib.pyplot as plt #Что это значит? (Зайцева П.)
#Ответ: это значит, что мы импортируем библиотеку matplotlib.pyplot, которая позволяет нам строить графики (Гошко Я.)
#Ответ правильный, 5 баллов (Зайцева П.)
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart8.png')


vals = Am_lst
labels = [str(x) for x in range(1,9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals, 
  labels = labels, 
  autopct = '%1.1f%%', 
  shadow = True, 
  explode = explode, 
  wedgeprops = {'lw':1, 'ls':'--', 'edgecolor': 'k'},
  rotatelabels = True  
)
ax.axis("equal")
plt.savefig('chart9.png')

vals = Am_lst_2
labels = [str(x) for x in range (1,9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals,
  labels = labels,
  autopct = '%1.1f%%',
  shadow = True,
  explode = explode,
  wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': "k"},
  rotatelabels = True
)
ax.axis("equal")
plt.savefig('chart10.png')

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.png')


#Индивидуальная часть 

#Контейнер расчета

from sympy import *
k, T, C, L = symbols('k C T L')

#пункт 1

C_ost = 1000000
Am_lst = []
C_ost_lst = []
for i in range(15):
  Am = (C - L)/T
  C_ost -= Am.subs({C: 1000000, T:15, L:0})
  Am_lst.append(round(Am.subs({C: 1000000, T:15, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am.lst:', C_ost_lst)
print('C_ost_lst:', C_ost_lst)

#пункт 2

Aj = 0
C_ost = 1000000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(15):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 1000000, T:15, k:2})
  Am_lst_2.append(round(Am.subs({C: 1000000, T:15, k:2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am.lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Пункт 3
#Линейный способ

from sympy import *
k, T, C, L =symbols("k C T L")

C_ost = 1000000
Am_lst = []
C_ost_lst = []
for i in range(15):
  Am = (C - L) / T
  C_ost -= Am.subs ({C:1000000, T:15, L:0})
  Am_lst.append(round(Am.subs({C: 1000000, T:15, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#Способ уменьшаемого остатка 

Aj = 0 
C_ost = 1000000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(15):
   Am = k * 1 / T * (C - Aj)
   C_ost -= Am.subs({C: 1000000, T:15, k:2})
   Am_lst_2.append(round(Am.subs({C: 1000000, T:15, k:2}), 2))
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода 

import pandas as pd
Y = range(1, 16)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#Контейнер визуализатора 

import numpy as np 
import matplotlib.pyplot as plt 
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart1.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart2.png')


vals = Am_lst
labels = [str(x) for x in range(1,16)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals, 
  labels = labels, 
  autopct = '%1.1f%%', 
  shadow = True, 
  explode = explode, 
  wedgeprops = {'lw':1, 'ls':'--', 'edgecolor': 'k'},
  rotatelabels = True  
)
ax.axis("equal")
plt.savefig('chart3.png')

vals = Am_lst_2
labels = [str(x) for x in range (1,16)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals,
  labels = labels,
  autopct = '%1.1f%%',
  shadow = True,
  explode = explode,
  wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': "k"},
  rotatelabels = True
)
ax.axis("equal")
plt.savefig('chart4.png')

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart5.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig('chart6.png')
"""""
#Индивидуальная часть (проверка целостности компонентов путем сравнения хэшей)

import json
import os
import sys
import hashlib
import argparse
from datetime import datetime
from typing import List, Dict, Any


try:
    import pandas as pd
    import matplotlib.pyplot as plt
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    print("Предупреждение: pandas/matplotlib не установлены. Графики не будут созданы.", file=sys.stderr)

# Настройки по умолчанию
DEFAULT_HASH_SECRET = "hash_secret_demo"
DEFAULT_DATA_FILE = "data.json"
DEFAULT_OUTPUT_DIR = "integrity_reports"

# Парсинг аргументов командной строки
def parse_arguments():
    parser = argparse.ArgumentParser(description="Контроль целостности компонентов (только хэш-сравнение)")
    parser.add_argument("--config", "-c", type=str, default=DEFAULT_DATA_FILE,
                        help=f"Путь к JSON-файлу с компонентами (по умолчанию {DEFAULT_DATA_FILE})")
    parser.add_argument("--secret", "-s", type=str, default=DEFAULT_HASH_SECRET,
                        help="Секрет для вычисления хэша")
    parser.add_argument("--output-dir", "-o", type=str, default=DEFAULT_OUTPUT_DIR,
                        help=f"Директория для сохранения отчётов и графиков")
    parser.add_argument("--no-viz", "-nv", action="store_true", help="Отключить создание графиков")
    return parser.parse_args()

# Создание выходной папки
def ensure_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Генерация примера data.json при первом запуске
def generate_example_config(filepath):
    example_data = [
        {"component_id": "cfg_app", "component_type": "config",
         "content": "database.host=localhost\ndatabase.port=5432",
         "reference_content": "database.host=localhost\ndatabase.port=5432"},
        {"component_id": "bin_worker", "component_type": "binary",
         "content": "#!/bin/bash\necho 'Worker started'",
         "reference_content": "#!/bin/bash\necho 'Worker started'"},
        {"component_id": "lib_crypto", "component_type": "library",
         "content": "def encrypt(data): return data",
         "reference_content": "def encrypt(data): return data"}
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(example_data, f, indent=2, ensure_ascii=False)
    print(f"[INFO] Создан пример конфигурации: {filepath}")

# Загрузка компонентов из JSON с проверкой обязательных полей
def load_components(filepath):
    if not os.path.exists(filepath):
        print(f"[ERROR] Файл {filepath} не найден.", file=sys.stderr)
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Корневой элемент JSON должен быть массивом")
    required_fields = {"component_id", "content", "reference_content"}
    for idx, item in enumerate(data):
        missing = required_fields - set(item.keys())
        if missing:
            raise KeyError(f"В элементе {idx} отсутствуют поля: {missing}")
    return data

# Вычисление SHA256 от строки с секретом
def compute_sha256_with_secret(content, secret):
    payload = (content + secret).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

# Основная функция проверки одного компонента 
def check_single_component(component, secret):
    current_hash = compute_sha256_with_secret(component["content"], secret)
    reference_hash = compute_sha256_with_secret(component["reference_content"], secret)
    hash_ok = (current_hash == reference_hash)
    return {
        "component_id": component["component_id"],
        "component_type": component.get("component_type", "unknown"),
        "hash_ok": hash_ok,
        "status": "OK" if hash_ok else "HASH_MISMATCH",
        "current_hash": current_hash,
        "reference_hash": reference_hash,
        "checked_at": datetime.now()
    }

# Текстовый отчёт в консоль
def print_text_report(results):
    total = len(results)
    ok_count = sum(1 for r in results if r["hash_ok"])
    fail_count = total - ok_count
    print("\nОТЧЁТ О ПРОВЕРКЕ ЦЕЛОСТНОСТИ")
    for r in results:
        status_marker = "✓" if r["hash_ok"] else "✗"
        print(f"{status_marker} {r['component_id']:20} -> {r['status']}")
    print(f"Всего проверено: {total}")
    print(f"Целостность подтверждена: {ok_count}")
    print(f"Нарушений: {fail_count}")
    if total > 0:
        print(f"Доля нарушений: {fail_count / total * 100:.1f}%")

# Визуализация результатов (графики)
def create_visualizations(results, output_dir):
    if not VISUALIZATION_AVAILABLE:
        return
    df = pd.DataFrame(results)
    df["checked_at"] = pd.to_datetime(df["checked_at"])
    df["status_ru"] = df["status"].map({"OK": "Норма", "HASH_MISMATCH": "Нарушение"})
    df["incident_flag"] = (df["status"] == "HASH_MISMATCH").astype(int)

    # 1. Круговая диаграмма распределения статусов
    plt.figure(figsize=(6, 6))
    df["status_ru"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Общая целостность компонентов")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "status_pie.png"), dpi=100)
    plt.close()

    # 2. Столбчатая диаграмма по типам компонентов
    if "component_type" in df.columns:
        crosstab = pd.crosstab(df["component_type"], df["status_ru"])
        if not crosstab.empty:
            ax = crosstab.plot(kind="bar", figsize=(8, 5))
            ax.set_title("Результаты проверки по типам компонентов")
            ax.set_xlabel("Тип компонента")
            ax.set_ylabel("Количество")
            plt.xticks(rotation=0)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, "by_type.png"), dpi=100)
            plt.close()

    # 3. График динамики нарушений во времени
    if len(df) > 1:
        plt.figure(figsize=(10, 4))
        plt.plot(df["checked_at"], df["incident_flag"], marker="o", linestyle="-", color="red")
        plt.title("Динамика нарушений целостности")
        plt.xlabel("Время проверки")
        plt.ylabel("Нарушение (0-норма, 1-нарушение)")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "timeline.png"), dpi=100)
        plt.close()

    print(f"[INFO] Графики сохранены в директорию: {output_dir}")

# Главная функция: запуск проверки, отчёт, визуализация
def run_integrity_check(config_file, secret, output_dir, disable_viz=False):
    ensure_output_dir(output_dir)
    if not os.path.exists(config_file):
        generate_example_config(config_file)
        print(f"[INFO] Отредактируйте {config_file} и запустите скрипт снова.")
        return
    components = load_components(config_file)
    results = []
    for comp in components:
        result = check_single_component(comp, secret)
        results.append(result)
        print(f"[CHECK] {result['component_id']}: {result['status']}")
    print_text_report(results)
    # Сохраняем детальный отчёт в JSON
    report_file = os.path.join(output_dir, f"integrity_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(report_file, "w", encoding="utf-8") as f:
        serializable_results = []
        for r in results:
            r_copy = r.copy()
            r_copy["checked_at"] = r_copy["checked_at"].isoformat()
            serializable_results.append(r_copy)
        json.dump(serializable_results, f, indent=2, ensure_ascii=False)
    print(f"[INFO] Детальный отчёт сохранён: {report_file}")
    # Визуализация, если не отключена
    if not disable_viz and VISUALIZATION_AVAILABLE:
        create_visualizations(results, output_dir)
    elif disable_viz:
        print("[INFO] Визуализация отключена пользователем.")


if __name__ == "__main__":
    args = parse_arguments()
    run_integrity_check(
        config_file=args.config,
        secret=args.secret,
        output_dir=args.output_dir,
        disable_viz=args.no_viz
    )