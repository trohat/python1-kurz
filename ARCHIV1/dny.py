week_days = { "Mon": "Tue",
              "Tue": "Wen",
              "Wen": "Thu",
              "Thu": "Fri",
              "Fri": "Sat",
              "Sat": "Sun",
              "Sun": "Mon",
              }


while True:
    today = input("Zadej den: ")
    if not today:
        break
    tomorrow = week_days[today]
    day_after_tomorrow = week_days[week_days[today]]

    print("Zítra je " + tomorrow)
    print("Pozítří je " + day_after_tomorrow)