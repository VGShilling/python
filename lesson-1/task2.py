sec = int(input("Введите время в секундах: "))
hour = (sec // 3600)
minutes = ((sec - (hour * 3600)) // 60)
seconds = (sec - (hour * 3600) - (minutes * 60))
print(f"{hour:02}:{minutes:02}:{seconds:02}")

