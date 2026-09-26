count = 0
while True:
    text = input("Enter temperature in Celsius (q to quit): ")
    if text == "q": #forgot ':' sytax error
        break
    celsius = float(text) #converted string to float

    fahrenheit = (celsius * 9) / 5 + 32 #fixed converting formula.
    count = count + 1
    print(f"{celsius} C = {fahrenheit} F")
print(f"You converted {count} temperatures.")
