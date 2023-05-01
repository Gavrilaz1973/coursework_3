import json
import datetime
from operator import itemgetter


def hide_numbers(volue: str):
    open_number = volue.split(' ')
    if len(open_number[-1]) == 16:
        open_number[-1] = open_number[-1][:4] + ' ' + open_number[-1][4:6] + '** **** ' + open_number[-1][12:]
    elif len(open_number[-1]) == 20:
        open_number[-1] = '**' + open_number[-1][16:]
    else:
        open_number[-1] = 'None'
    return ' '.join(open_number)


def last_5_operations(data: list):
    data_sorted = []

    for item in data:
        if 'date' in item:
            if item['state'] == 'EXECUTED':
                item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
                data_sorted.append(item)

    sorted(data_sorted, key=itemgetter('date'), reverse=True)
    result = ''
    for i in range(5):
        if 'from' not in data_sorted[i]:
            data_sorted[i]['from'] = 'None'
        result += f"\n{data_sorted[i]['date'].strftime('%d.%m.%Y')} {data_sorted[i]['description']}\n" \
               f"{hide_numbers(data_sorted[i]['from'])} -> {hide_numbers(data_sorted[i]['to'])}\n" \
               f"{data_sorted[i]['operationAmount']['amount']} {data_sorted[i]['operationAmount']['currency']['name']}\n"
    return result


if __name__ == '__main__':
    file = open("operations.json")
    data = json.load(file)
    print(last_5_operations(data))
