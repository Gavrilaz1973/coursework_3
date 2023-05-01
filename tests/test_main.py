import pytest

import main


def test_hide_numbers():
    assert main.hide_numbers("Master card 1234567898765432") == 'Master card 1234 56** **** 5432'
    assert main.hide_numbers("Счет 12345678987654322345") == 'Счет **2345'
    assert main.hide_numbers("Счет 123456789654322345") == 'Счет None'

@pytest.fixture
def data_positive():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]


def test_last_5_operations(data_positive):
    with pytest.raises(IndexError):
        type(main.last_5_operations(data_positive)) == str

