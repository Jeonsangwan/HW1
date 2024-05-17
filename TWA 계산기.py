# 유해인자의 종류 입력
Type_of_Hazardous_Substances = input("유해인자의 종류를 입력하세요: ")

# 유해인자의 측정치와 시간을 입력
measurements = []  # (시간, 유해인자 측정치) 튜플을 저장할 리스트

while True:
    time_str = input("시간을 입력하세요 (종료하려면 'q' 입력): ")
    if time_str == 'q':
        break
    try:
        hour = float(time_str)
    except ValueError:
        print("유효한 시간을 입력하세요.")
        continue
    try:
        concentration = float(input(f"{hour}시간 동안의 유해인자의 측정치를 입력하세요: "))
    except ValueError:
        print("유효한 농도를 입력하세요.")
        continue
    measurements.append((hour, concentration))

# 분자 계산
numerator = sum([hour * concentration for hour, concentration in measurements])

# 분모 계산
denominator = sum([hour for hour, _ in measurements])

# 유해인자의 단위 설정
if Type_of_Hazardous_Substances == "분진" :
    unit = "mg/m^3"
elif Type_of_Hazardous_Substances == "가스" :
    unit = "ppm"
else :
    unit = "unknown"

# 시간가중 평균 농도 계산
TWA = numerator / denominator

# 결과 출력
print(f"유해인자 종류 : {Type_of_Hazardous_Substances}")
print(f"시간가중 평균 농도는 {TWA:.2f} {unit}입니다.")
