def main():
    dollars = dollars_to_float(input("How much was the meal?\n"))
    percent = percent_to_float(input("What percentage would you like to tip?\n"))
    tip = dollars * percent
    print (f"leave ${tip:.2f}")
def dollars_to_float(dollars_to_float):
    float_value = float(dollars_to_float.lstrip('$'))
    return float_value
def percent_to_float(percent_to_float):
    percent_value = float(percent_to_float.rstrip('%'))
    tip_percent = percent_value /100
    return tip_percent

main()