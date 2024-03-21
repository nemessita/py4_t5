# Səhiyyə Sənayesi:
# Tapşırıq: BMI Kalkulyatorunu tərtib edin.
# Təsvir: Python funksiyalarından istifadə edərək Bədən Kütləsi İndeksi (BMI) kalkulyatoru yaradın. 
# İstifadəçilərdən parametr olaraq çəkilərini (kiloqramla) və 
# boylarını (metrlə) daxil etmələri təklif edilməlidir və proqram BMI-ni hesablayıb çap etməlidir. 
# Əlavə olaraq, istifadəçiyə BMI kateqoriyası 
# (məsələn, az çəki, normal çəki, artıq çəki və ya piylənmə) haqqında rəy bildirin.




def my_def(height, weight):
    bmi = round(weight / height ** 2, 1)
    if bmi < 18.5:
        return quality["az çəki"]
    elif 18.5 <= bmi < 25:
        return quality["normal çəki"]
    elif 25 <= bmi < 30:
        return quality["artıq çəki"]
    else:
        return quality["piylənmə"]

quality = {
    "az çəki": "Az çəki",
    "normal çəki": "Normal çəki",
    "artıq çəki": "Artıq çəki",
    "piylənmə": "Piylənmə"
}

height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

result = my_def(height, weight)
print("Your BMI category is:", result)




