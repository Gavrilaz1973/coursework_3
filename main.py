import json
import datetime
from operator import itemgetter


def last_5_operations(data:list):
    data_sorted = []

    for item in data:
        if 'date' in item:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
            data_sorted.append(item)

    sorted(data_sorted, key=itemgetter('date'), reverse=True)

    for i in range(5):
        if 'from' not in data_sorted[i]:
            data_sorted[i]['from'] = 'None'
        print(f"\n{data_sorted[i]['date'].strftime('%d.%m.%Y')} {data_sorted[i]['description']}")
        print(f"{data_sorted[i]['from']} -> {data_sorted[i]['to']}")
        print(
            f"{data_sorted[i]['operationAmount']['amount']} {data_sorted[i]['operationAmount']['currency']['name']}\n")

if __name__ == '__main__':
    file = open("operations.json")
    data = json.load(file)
    last_5_operations(data)