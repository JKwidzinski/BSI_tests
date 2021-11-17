"""
Program was created by Jakub Kwidziński and Jeremi Rycharski.
All rights reserved.
"""
import math
def reliability_const_fail():
    """This is a function that allows calculating the reliability with the given failure rate and operational time.
    
    Arguments():
        const_fail (float): Constant failure rate of an item.
        time (float): Number of hours of continous service. 
   
    Returns:
        (string): String that contains the reliability value.
    """  
    const_fail, time =[float(x) for x in input("Enter constant failure rate and time: ").split(" ")]
    return float('{:.10f}'.format(math.exp((-1)*const_fail*time)))

def highest_failure_rate():
    """This is a function that calculates the highest failure rate for a product, when given the reliability and time.
    
    Arguments:
        reliability (float): Reliability of an item.
        time (float): Number of hours at which the reliability is achieved.
    
    Returns:
        (string): String that contains the highest failure rate value.
    """
    reliability, time = [float(x) for x in input("Enter reliability and time: ").split(" ")]
    return float('{:.10f}'.format(math.log(reliability)/time*(-1)))

def mtbf_failure_rate():
    """This is a function that calculates constant failure rate, when given the mtbf of a item.
    
    Arguments:
        mtbf (float): Mean time before failure of an item.
    
    Returns:
        (float): Returns failure rate of an item.
    """
    mtbf = float(input("Enter mtbf: "))
    return float('{:.4f}'.format(1/mtbf))

def item_reliability():
    """This is a function that achieves the correct mathematical formula for a reliability function when only MTBF is  given. Then, in the second step, by giving time (t), we are able to calculate the reliability of a given item.
    
    Arguments:
        time (float): Time at which the reliability of an item is calculated.
    
    Returns:
        (string): Returns a string with the reliability value.
    """
    fail_rate = mtbf_failure_rate()
    print("R(t)=e^-({}*t)".format(fail_rate))
    time = float(input("Enter time: "))
    return float('{:.10f}'.format(math.exp((-1)*fail_rate*time)))

def probability_without_fail():
    """This is a function that calculates the probability of an item operating after given time by percentage.
    
    Arguments:
        time (float): Time for which this function calculates probability for.
    
    Returns:
        (string): Returns string that contains the probability of an item operating after given time by percentage. 
    """
    fail_rate = mtbf_failure_rate()
    time = float(input("Enter time: "))
    return '{:.0%}'.format(math.exp((-1)*fail_rate*time))

def units_fail_in_year(fail_rate, unit_amount, time):
    """This is a function that calculates number of units that failed during chosen year. 
    
    Arguments:
        fail_rate (float): Constant failure rate of an item.
        unit_amount (float): Number of units.
        time (float): Number of years. 
        chosen_year (int)(via input): Year that user chose to calculate number of units failed for.
    
    Returns:
        fail_chosen_year (float): Returns a number of units that failed during chosen year.
        chosen_year (int): Returns a year chosen by an user.
    """
    chosen_year = int(input("Enter year you chose: "))
    while chosen_year<1 and chosen_year>time:
        chosen_year = int(input("Enter year you chose: "))
    
    for i in range(int(time)):
        if i == (chosen_year-1):
            fail_chosen_year = unit_amount*fail_rate
            
        unit_amount -= (unit_amount*fail_rate)
        
    return int(fail_chosen_year)

def remaining_units():
    """This is a function that calculates amount of remaining units after a given period of time.
    
    Arguments(via input):
        fail_rate (float): Fail rate of an item.
        unit_amount (float): Amount of items.
        time (float): Period of time that the amount of remaining units is calculated for.

    Returns:
        (string): Returns a string that contains the amount of remaining units and amount of items that failed druing chosen year.
    """
    fail_rate, unit_amount, time = [float(x) for x in input("Enter constant failure rate, number of units and number of years: ").split(" ")]
    initial_unit_amount = unit_amount
    unit_amount *= math.exp((-1)*fail_rate*time)
    fail_chosen_year = units_fail_in_year(fail_rate, initial_unit_amount, time)
    return int(unit_amount), int(fail_chosen_year)