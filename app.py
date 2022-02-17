import sys
import pandas as pd


def vowel_count(text):
    text = text.lower()
    count = 0
    vowels = set("aeiou")
    for char in text:
        if char in vowels:
            count += 1
    return count


def consonant_count(text):
    text = text.lower()
    count = 0
    vowels = set("bcdfghjklmnpqrstvxyz")
    for char in text:
        if char in vowels:
            count += 1
    return count


def fileToArray(path):
    file = open(path, 'r')
    lines = file.read().split('\n')
    file.close()
    return lines


def commonFactor(num1, num2):
    small = min(num1, num2)
    for i in range(2, small+1):
        if (num1 % i == 0 and num2 % i == 0):
            return True
    return False


def topSecretAlgoritm(destinationArry, driverArr):

    table_destination = []
    table_drivers = []
    table_ss = []
    for destination in destinationArry:
        driver_dest_ss = []
        for driver in driverArr[:]:
            destinationLength = len(destination.replace(" ", ""))
            driverLength = len(driver.replace(" ", ""))
            if destinationLength % 2 == 0:
                vcount = vowel_count(driver)
                ss = vcount*1.5
            else:
                ccount = consonant_count(driver)
                ss = ccount

            _commonFactor = commonFactor(destinationLength, driverLength)
            if _commonFactor:
                ss = ss+ss*.5

            driver_dest_ss.append(ss)
        # GETTING THE MAX SS VALUE
        max_value = max(driver_dest_ss)
        max_index = driver_dest_ss.index(max_value)

        # ADDING DESTINATION TO THE FINAL DESTINATION ARRAY
        table_destination.append(destination)
        # ADDING DRIVER TO THE FINAL DRIVERS ARRAY
        table_drivers.append(driverArr[max_index])
        # ADDING SS VALUE TO THE FINAL SS ARRAY
        table_ss.append(max_value)
        del driverArr[max_index]

    data = {'Destination': table_destination,
            'Driver': table_drivers,
            'SS': table_ss}
    return data


def main():
    try:
        destination_path = sys.argv[1]
        drivers_path = sys.argv[2]
        destination_array = fileToArray(destination_path)
        drivers_array = fileToArray(drivers_path)
        data = topSecretAlgoritm(destination_array, drivers_array)

        table = pd.DataFrame(data)
        print(table)
    except Exception as e:
        print(
            "An error occurred please check that you have entered the file paths correctly")


if __name__ == "__main__":
    main()
