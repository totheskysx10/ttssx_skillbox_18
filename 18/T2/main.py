import re

car_numbers = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"

private_car_pattern = re.compile(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}")
taxis_car_pattern = re.compile(r"[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}")

print(f"Список номеров частных автомобилей: {re.findall(private_car_pattern, car_numbers)}")
print(f"Список номеров такси: {re.findall(taxis_car_pattern, car_numbers)}")