def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5 ) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * 5 / 9 
def main():
    while True:
        user_input = input("Enter 'C' ,'F' OR 'Q ' Only :").upper()
        if user_input == "Q":
            print("Thank you have a grat day !")
            break
        elif user_input == "C":
            celsius = float(input("Enter 'C' to convert Fahrenheit :"))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} is {fahrenheit}")
        elif user_input == "F":
            fahrenheit = float(input("Enter 'F' to convert celsius :"))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} is {celsius}")
        else:
            print("Please Enter Correct letter code to continue:")
if __name__ == "__main__":
    main()
            