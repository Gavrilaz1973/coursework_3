import main


def test_hide_numbers():
    assert main.hide_numbers("Master card 1234567898765432") == 'Master card 1234 56** **** 5432'
    assert main.hide_numbers("Счет 12345678987654322345") == 'Счет **2345'
    assert main.hide_numbers("Счет 123456789654322345") == 'Счет None'


