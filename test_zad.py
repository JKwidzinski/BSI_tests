import zad
import pytest

#reliability_const_fail

@pytest.mark.parametrize('input, result',
                         [
                             ('0.000001 2500', 0.9975031224),
                             ('0.00001 2000', 0.9801986733),
                             ('0.0008 2000', 0.2018965180),                       
                         ]
    
)
def test_reliability_const_fail_num(input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.reliability_const_fail() == result
    
@pytest.mark.parametrize('input',
                         [
                             ('a b'),
                             ('2 a'),
                             ('a 2')
                         ]
)    
def test_reliability_const_fail_char(input, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: input)
        zad.reliability_const_fail()
    

@pytest.mark.parametrize('input, result',
                         [
                             ('-0.000001 2500', 1.0025031276),
                             ('0.000001 -2500', 1.0025031276),
                             ('-0.000001 -2500', 0.9975031224)
                         ]
)    
def test_reliability_const_fail_negative(input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.reliability_const_fail() == result
    pytest.xfail("Function only works for numbers that aren't negative")

#highest_failure_rate
    
@pytest.mark.parametrize('input, result',
                         [
                             ('0.98 5000', 0.0000040405),
                             ('0.975 4000', 0.0000063295),
                             ('0.978 2000', 0.0000111228)   
                         ]
)
def test_highest_failure_rate(input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.highest_failure_rate() == result

@pytest.mark.parametrize('input',
                         [
                             ('a b'),
                             ('2 a'),
                             ('a 2')
                         ]
)    
def test_highest_failure_rate_char(input, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: input)
        zad.highest_failure_rate()
    
@pytest.mark.parametrize('input, result',
                         [
                             ('0.98 -5000', -0.0000040405),
                             ('0.975 -4000', -0.0000063295),
                             ('0.978 -2000', -0.0000111228)   
                         ]
)
def test_highest_failure_rate_negative(input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.highest_failure_rate() == result
    pytest.xfail("Function only works for numbers that aren't negative")
    
@pytest.mark.parametrize('input',
                         [
                             ('-0.98 -5000'),
                             ('-0.975 4000'),
                             ('-0.978 2000')   
                         ]
)
def test_highest_failure_rate_negative_reliability(input, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: input)
        zad.highest_failure_rate()
        
#mtbf_failure_rate
@pytest.mark.parametrize('input, result',
                         [
                             ('25', 0.04),
                             ('30', 0.0333),
                             ('50', 0.02)
                         ]
)
def test_mtbf_failure_rate(input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.mtbf_failure_rate() == result
    
@pytest.mark.parametrize('input, result',
                         [
                             ('-25', -0.04),
                             ('-30', -0.0333),
                             ('-50', -0.02)   
                         ]
)
def test_mtbf_failure_rate_negative(input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.mtbf_failure_rate() == result
    pytest.xfail("Function only works for numbers that aren't negative")
    
@pytest.mark.parametrize('input',
                         [
                             ('a'),
                             ('$'),
                             ('XP')
                         ]
)    
def test_highest_failure_rate_char(input, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: input)
        zad.highest_failure_rate()
        
#item_reliability

@pytest.mark.parametrize('input1, input2, result',
                         [
                             ('25', '30', 0.3682475046),
                             ('30', '40', 0.3678794412),
                             ('50', '70', 0.3675117456)
                         ]
)
def test_item_reliability(input1, input2, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    assert zad.item_reliability() == result
    
@pytest.mark.parametrize('input1, input2',
                         [
                             ('ab', 'c'),
                             ('30', 'xd'),
                             ('axd', 'bT%#@')
                         ]
)
def test_item_reliability_char1(input1, input2, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda a: input1)
        monkeypatch.setattr('builtins.input', lambda b: input2)
        zad.item_reliability()
        
@pytest.mark.parametrize('input1, input2',
                         [
                             ('ab', 'c'),
                             ('30', 'xd'),
                             ('axd', 'bT%#@')
                         ]
)
def test_item_reliability_char2(input1, input2, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    pytest.xfail("Function only works for numbers")
    zad.item_reliability()
    
@pytest.mark.parametrize('input1, input2',
                         [
                             ('-25', '30'),
                             ('30', '-40'),
                             ('-50', '-70')
                         ]
)
def test_item_reliability_negative(input1, input2, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    pytest.xfail("Function only works for numbers that aren't negative")
    zad.item_reliability()
    
#probability_without_fail
@pytest.mark.parametrize('input1, input2, result',
                         [
                             ('25', '30', '37%'),
                             ('30', '40', '37%'),
                             ('50', '70', '37%')
                         ]
)
def test_probability_without_fail(input1, input2, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    assert zad.probability_without_fail() == result
    
@pytest.mark.parametrize('input1, input2',
                         [
                             ('ab', 'c'),
                             ('30', 'xd'),
                             ('axd', 'bT%#@')
                         ]
)
def test_probability_without_fail_char1(input1, input2, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda a: input1)
        monkeypatch.setattr('builtins.input', lambda b: input2)
        zad.probability_without_fail()

@pytest.mark.parametrize('input1, input2',
                         [
                             ('ab', 'c'),
                             ('30', 'xd'),
                             ('axd', 'bT%#@')
                         ]
)
def test_probability_without_fail_char2(input1, input2, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    pytest.xfail("Function only works for numbers")
    zad.probability_without_fail()
    
@pytest.mark.parametrize('input1, input2',
                         [
                             ('-25', '30'),
                             ('30', '-40'),
                             ('-50', '-70')
                         ]
)
def test_probability_without_fail_negative(input1, input2, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    pytest.xfail("Function only works for numbers that aren't negative")
    zad.probability_without_fail()
             
#units_fail_in_year

@pytest.mark.parametrize('fail_rate, unit_amount, time, input, result',
                         [
                             (0.05, 1000, 5, '5', 40),
                             (0.07, 1000, 7, '7', 45),
                             (0.11, 1000, 4, '4', 77)
                         ]
)
def test_units_fail_in_year(fail_rate, unit_amount, time, input, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    assert zad.units_fail_in_year(fail_rate, unit_amount, time) == result

@pytest.mark.parametrize('fail_rate, unit_amount, time, input',
                         [
                             (-0.05, 1000, 5, '5'),
                             (0.07, -1000, 7, '7'),
                             (0.11, 1000, -4, '4'),
                             (0.11, 1000, 4, '-4')
                         ]
)
def test_units_fail_in_year_negative(fail_rate, unit_amount, time, input, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input)
    pytest.xfail("Function only works for numbers that aren't negative")
    zad.units_fail_in_year(fail_rate, unit_amount, time)       

@pytest.mark.parametrize('fail_rate, unit_amount, time, input',
                         [
                             ('a', 1000, 5, '5'),
                             (0.07, 'a', 7, '7')
                         ]
)
def test_units_fail_in_year_char1(fail_rate, unit_amount, time, input, monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setattr('builtins.input', lambda _: input)
        zad.units_fail_in_year(fail_rate, unit_amount, time)

@pytest.mark.parametrize('fail_rate, unit_amount, time, input',
                         [
                             (0.11, 1000, 'a', '4'),
                             (0.11, 1000, 4, 'a')
                         ]
)
def test_units_fail_in_year_char2(fail_rate, unit_amount, time, input, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: input)
        zad.units_fail_in_year(fail_rate, unit_amount, time)

#remaining_units

@pytest.mark.parametrize('input1, input2, result',
                         [
                             ('0.05 1000 5', '5', [778, 40]),
                             ('0.07 1000 7', '7', [612, 45]),
                             ('0.11 1000 4', '4', [644, 77])
                         ]
)
def test_remaining_units(input1, input2, result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    assert zad.remaining_units() == result

@pytest.mark.parametrize('input1, input2',
                         [
                             ('-0.05 1000 5', '5'),
                             ('0.07 -1000 7', '7'),
                             ('0.11 1000 -4', '4')
                         ]
)
def test_remaining_units_negative(input1, input2, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: input1)
    monkeypatch.setattr('builtins.input', lambda b: input2)
    pytest.xfail("Function only works for numbers that aren't negative")
    zad.remaining_units()

@pytest.mark.parametrize('input1, input2',
                         [
                             ('a 1000 5', '5'),
                             ('0.07 a 7', '7'),
                             ('0.11 1000 a', '4')
                         ]
)
def test_remaining_units_char(input1, input2, monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda a: input1)
        monkeypatch.setattr('builtins.input', lambda b: input2)
        zad.remaining_units() 
