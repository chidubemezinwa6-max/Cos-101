# STUDENT 3 - PHYSICS CALCULATOR

def frequency():
    cycles = float(input("Enter number of cycles: "))
    time = float(input("Enter time: "))
    if time > 0:
        print("Frequency =", cycles / time, "Hz")
    else:
        print("Invalid time")

def period():
    freq = float(input("Enter frequency: "))
    if freq > 0:
        print("Period =", 1 / freq, "seconds")
    else:
        print("Frequency must be positive")

def wave_speed():
    wavelength = float(input("Enter wavelength: "))
    freq = float(input("Enter frequency: "))
    print("Wave speed =", wavelength * freq, "m/s")

def electric_current():
    charge = float(input("Enter electric charge: "))
    time = float(input("Enter time: "))
    if time > 0:
        print("Electric current =", charge / time, "Amperes")
    else:
        print("Invalid time")

def voltage():
    resistance = float(input("Enter resistance: "))
    current = float(input("Enter current: "))
    print("Voltage =", resistance * current, "Volts")

while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Frequency")
    print("2. Time Period")
    print("3. Wave Speed")
    print("4. Electric Current")
    print("5. Voltage")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        frequency()
    elif choice == "2":
        period()
    elif choice == "3":
        wave_speed()
    elif choice == "4":
        electric_current()
    elif choice == "5":
        voltage()
    else:
        print("Invalid choice")

    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != "yes":
        print("Goodbye!")
        break
