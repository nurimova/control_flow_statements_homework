def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<10:
        return "Muzlab qoladi"
    if -1<temp<10:
        return "Juda sovuq"
    if 11<temp<20:
        return "Sovuq"
    if 21<temp<30:
        return "Normal"
    if 31<temp<40:
        return "issiq"
    if temp>40:
        return "juda issiq"
print(main(13))