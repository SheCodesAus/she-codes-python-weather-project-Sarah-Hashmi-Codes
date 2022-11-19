import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    return(date.strftime("%A %d %B %Y"))
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


def convert_f_to_c(temp_in_farenheit):
    temp_in_farenheit = (float(temp_in_farenheit)-32)*(5/9)
    return round(temp_in_farenheit,1)
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass


def calculate_mean(weather_data):
    temperatures = 0
    for count in weather_data:
        temperatures += float(count)
    return (temperatures / len(weather_data))
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass


def load_data_from_csv(csv_file):
    weather_data=[]
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        # csv_reader=list(csv_reader)
        print(csv_reader)
        for row in csv_reader:
            if row == []:

                continue

            date, min, max = row
            weather_data.append([date, float(min), float(max)])
    return weather_data
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    if weather_data == []:
        return ()
    else:
        min_temp = weather_data[0]
        min_temp_idx = 0
        counter = 0
        for temp in weather_data:
            if float(temp) <= float(min_temp):
                min_temp = float(temp)
                min_temp_idx = counter
            counter += 1

        return(min_temp,min_temp_idx)
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    if weather_data == []:
        return ()
    else:
        max_temp = weather_data[0]
        max_temp_idx = 0
        counter = 0
        for temp in weather_data:
            if float(temp) >= float(max_temp):
                max_temp = float(temp)
                max_temp_idx = counter
            counter += 1

        return(max_temp,max_temp_idx)



    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    summary= ""
    low = []
    high = []
    for row in weather_data:
        low.append(row[1])
        high.append(row[2])

    summary = f"{len(weather_data)} Day Overview\n\
  The lowest temperature will be {format_temperature(convert_f_to_c(find_min(low)[0]))}, and will occur on {convert_date(weather_data[find_min(low)[1]][0])}.\n\
  The highest temperature will be {format_temperature(convert_f_to_c(find_max(high)[0]))}, and will occur on {convert_date(weather_data[find_max(high)[1]][0])}.\n\
  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(low)))}.\n\
  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(high)))}.\n"

    return summary

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    daily_sum = ""
    for row in weather_data:
        date = f"---- {convert_date(row[0])} ----\n"
        min_formated_temp= f"  Minimum Temperature: {format_temperature(convert_f_to_c(row[1]))}\n"
        max_formated_temp= f"  Maximum Temperature: {format_temperature(convert_f_to_c(row[2]))}\n"
        daily_sum += date + min_formated_temp + max_formated_temp +"\n"
    return daily_sum

    
    # print(f"  Minimum Temperature: {min_formated_temp}")
    # print(f"  Maximum Temperature: {max_formated_temp}")
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
