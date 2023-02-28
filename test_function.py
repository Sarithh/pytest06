from function import number_to_month,validate_number
import pytest 

@pytest.mark.code 
def test_january_input1():
    input = 1 
    expected_result = "January"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_february_input2():
    input = 2
    expected_result = "February"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_march_input3():
    input = 3
    expected_result = "March"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_april_input4():
    input = 4
    expected_result = "April"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_may_input5():
    input = 5
    expected_result = "May"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_june_input6():
    input = 6
    expected_result = "June"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.code 
def test_july_input7():
    input = 7
    expected_result = "July"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_august_input8():
    input = 8
    expected_result = "August"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_september_input9():
    input = 9
    expected_result = "September"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_october_input10():
    input = 10
    expected_result = "October"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_november_input11():
    input = 11
    expected_result = "November"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_december_input12():
    input = 12
    expected_result = "December"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_out_of_range_input0():
    input = 0
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_out_of_range_input13():
    input = 13
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_out_of_range_input_minus_10():
    input = -10
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate #pytest -m validate
def test_out_of_range_input_22():
    input = 22
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_input_integer_input_1_1():
    input = 1.1
    expected_result = "Input Integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_out_of_range_input_13_1():
    input = 13.1
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_input_integer_input_char_a():
    input = "a"
    expected_result = "Input Integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_input_integer_input_char_sharp():
    input = "#"
    expected_result = "Input Integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate #pytest -m validate
def test_1_input_1():
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_12_input_12():
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_out_of_range_input_0_5():
    input = 0.5
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_out_of_range_input_minus_1_5():
    input = -1.5
    expected_result = "Out of Range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate #pytest -m validate
def test_input_integer_input_1_5():
    input = 1.5
    expected_result = "Input Integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result