#예제4
import random
hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))
#반복문 한 줄씩 읽기
with open("info.txt", "r") as file:
    for line in file:
        # 변수를 선언
        (name, weight, height) = line.strip().split(", ")

        # 데이터가 문제없는지 확인, 문제가 있으면 지나감
        if (not name) or (not weight) or (not height):
            continue

        # 결과 계산
        bmi = int(weight) / ((int(height) / 100) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()