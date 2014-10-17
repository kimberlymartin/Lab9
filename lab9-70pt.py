#70pt

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "What's the temperature in Celcius?"
celcius = int(raw_input())
fahrenheit = ((celcius * 9) / 5) + 32
print "The temperature is " + str(fahrenheit) + " degrees fahrenheit."