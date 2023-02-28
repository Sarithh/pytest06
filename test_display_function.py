from function import display_month
import pytest 

@pytest.mark.display #pytest -m display
@pytest.mark.parametrize('input_number,expected_result', [
    (1,"January"),(2,"February"),(3,"March"),(4,"April"),(5,"May"),(6,"June"),(7,"July"),(8,"August"),(9,"September"),(10,"October"),(11,"November"),(12,"December"),(0,"Out of Range"),(13,"Out of Range"),(-10,"Out of Range"),(22,"Out of Range"),
    (1.1,"Input Integer"),(13.1,"Out of Range"),("a","Input Integer"),("#","Input Integer"),(0.5,"Out of Range"),(-1.5,"Out of Range"),(1.5,"Input Integer")
    ])
def test_display(input_number,expected_result):
    actual_result = display_month(input_number)
    assert expected_result == actual_result

