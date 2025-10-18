def space_mission_analysis():
    planets = (
        ("Меркурий", 2439, 3.3e23),
        ("Венера", 6051, 4.9e24),
        ("Земля", 6371, 6.0e24),
        ("Марс", 3389, 6.4e23),
        ("Юпитер", 69911, 1.9e27)
    )

    temperature_measurements = [
        [167, 437, 465],  
        [437, 464, 500],  
        [-89, 15, 57],    
        [-153, -63, 20],  
        [-163, -108, -80] 
    ]
    
    print("АНАЛИЗ КОСМИЧЕСКОЙ МИССИИ")
    print("=" * 50)

    print("\n ДАННЫЕ О ПЛАНЕТАХ:")
    for i, (name, radius, mass) in enumerate(planets):
        print(f"{i+1}. {name}:")
        print(f"   Радиус: {radius:,} км")
        print(f"  Масса: {mass:.1e} кг")
        print(f"  Температуры: {temperature_measurements[i][0]}°C (мин), "
              f"{temperature_measurements[i][1]}°C (сред), "
              f"{temperature_measurements[i][2]}°C (макс)")
    
    max_temp_range = 0
    planet_with_max_range = ""
    
    for i, (name, _, _) in enumerate(planets):
        temp_range = temperature_measurements[i][2] - temperature_measurements[i][0]
        if temp_range > max_temp_range:
            max_temp_range = temp_range
            planet_with_max_range = name
    
    print(f"\n Наибольший перепад температур: {planet_with_max_range} ({max_temp_range}°C)")
    
    print("\n ПОЛУЧЕНЫ НОВЫЕ ДАННЫЕ!")
    new_measurements = [-170, -120, -75] 
    temperature_measurements[4] = new_measurements
    
    print("Обновленные данные по Юпитеру:")
    print(f"Температуры: {temperature_measurements[4][0]}°C (мин), "
          f"{temperature_measurements[4][1]}°C (сред), "
          f"{temperature_measurements[4][2]}°C (макс)")
    
    mission_report = (
        "Отчет космической миссии",
        f"Исследовано планет: {len(planets)}",
        f"Планета с максимальным радиусом: {max(planets, key=lambda x: x[1])[0]}",
        f"Планета с максимальной массой: {max(planets, key=lambda x: x[2])[0]}",
        f"Самая экстремальная по температуре: {planet_with_max_range}"
    )
    
    print("\n ИТОГОВЫЙ ОТЧЕТ МИССИИ:")
    for line in mission_report:
        print(f"   • {line}")
    
    return planets, temperature_measurements

if __name__ == "__main__":
    planets_data, temp_data = space_mission_analysis()
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ СВОЙСТВ ДАННЫХ:")
    
    try:
        planets[0] = ("Нептун", 24622, 1.02e26)
    except TypeError as e:
        print(" Кортеж нельзя изменить:", e)
    
    print("Список можно изменять:")
    print("До изменения:", temp_data[0])
    temp_data[0][1] = 450 
    print("После изменения:", temp_data[0])