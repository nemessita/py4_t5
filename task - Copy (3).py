# Təhsil Sənayesi:
# Tapşırıq: Tələbə Qiymət Kalkulyatoru.
# Təsvir: Müxtəlif fənlər üzrə topladıqları ballara əsasən tələbələrin qiymətlərini hesablamaq 
# üçün proqram yaradın. İstifadəçidən hər bir fənn üzrə xalları daxil etməyi, orta qiyməti hesablamağı 
# və onların fəaliyyəti haqqında rəy bildirməyi təklif edin (məsələn, məktub qiymətləri). 
# Orta hesablamaq və qiyməti müəyyən etmək üçün funksiyalardan istifadə edin 
# və qiymətləndirmə meyarları üçün if-else ifadələrini birləşdirin. 
# Qeyd: Bu taskdan bütün biliklərinizi maksimum istifadə edin və məntiqli kod yazmağa çalışın


def my_def(lesson, mark):
    if 90 <= mark <= 100:
        print("Excellent")
    elif 80 <= mark < 90:
        print("Good")
    elif 70 <= mark < 80:
        print("Normal")
    elif 60 <= mark < 70:
        print("Bad")
    else:
        print("Fail")


lessons = {
    "english": 0,
    "math": 1,
    "physics": 2,
    "chemistry": 3
}

for lesson, mark in lessons.items():
    mark = int(input(f"Enter mark for {lesson}: "))
    my_def(lesson, mark)















