import random
from random import uniform, choice
import csv

# список датчиков и нормадбных значений
list_of_frames = [('Давление в водяном охлаждении', (3.5, 4)), ('Давление масла', (2.5, 3.5)),
                  ('Температура воды после охлаждения поршней', (60, 90)),
                  ('Температура выпускных газов на выходе из цилиндра', (400, 410)),
                  ('Температура масла на входе в двигатель', (40, 50)),
                  ('Температура охлаждающей воды на входе в дизель', (68, 78)),
                  ('Вязкость тяжёлого топлива на входе в дизель', (10, 15))]


# функция получения списка датчиков
def return_lst_of_frames():
    return list_of_frames


# создание файлов с данными датчиков
def create_db():
    # создание случайных данных для примера работы
    for frame, value in list_of_frames:
        minimum, maximum = value
        data = []
        for i in range(15000):
            data_dict = {'Value': None,
                         frame: None}
            if random.randrange(4) == 1:
                n = choice((0.25, -0.25))
                data_dict['Value'] = float(i)
                data_dict[frame] = uniform(minimum, maximum) + maximum * n
            else:
                data_dict['Value'] = float(i)
                data_dict[frame] = uniform(minimum, maximum)

            data.append(data_dict)

        with open(f'data/datasets/data_{frame}.csv', 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL, fieldnames=list(data[0].keys())
            )
            writer.writeheader()
            for elem in data:
                writer.writerow(elem)
