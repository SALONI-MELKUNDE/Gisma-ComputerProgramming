temperature = 25

def thermostat_regulator(temperature, low_temp=20, high_temp=27):
    if temperature < low_temp:
        state = 'Turn on heater'
    elif temperature > high_temp:
        state = 'Turn on cooler'
    elif temperature > low_temp and temperature < high_temp:
        state = 'Do nothing'
    print(state)
    return state

state = thermostat_regulator(temperature)

# Define a temperature value before calling the function
#temp = 25  # Uncommented and assigned a value
#state = thermostat_regulator(temp)  # Passing the temperature as an argument








