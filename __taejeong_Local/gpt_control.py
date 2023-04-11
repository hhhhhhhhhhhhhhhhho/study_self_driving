import time
from adafruit_motorkit import MotorKit
import serial

# 시리얼 통신 설정
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# 모터 드라이버 설정
kit = MotorKit()

# 모터 제어 함수
def drive(left_speed, right_speed):
    kit.motor1.throttle = left_speed
    kit.motor2.throttle = right_speed

# 조향각 제어 함수
def steer(angle):
    ser.write((str(angle) + '\n').encode())
    response = ser.readline().strip()
    return response

# 경로 정보를 저장한 리스트
path = [(37.123, 127.456), (37.234, 127.567), (37.345, 127.678), (37.456, 127.789)]

# 현재 위치 정보를 받아오는 함수
def get_current_location():
    # GPS 정보를 받아옴
    latitude, longitude = (37.123, 127.456)  # 예시를 위해 임의의 값 설정
    return latitude, longitude

# 현재 위치에서 가장 가까운 경로 점을 찾는 함수
def find_nearest_point(current_location):
    nearest_point = path[0]
    nearest_distance = get_distance(current_location, path[0])
    for point in path[1:]:
        distance = get_distance(current_location, point)
        if distance < nearest_distance:
            nearest_point = point
            nearest_distance = distance
    return nearest_point

# 두 점 사이의 거리를 계산하는 함수
def get_distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    radius = 6371  # 지구 반지름 (km)
    dlat = (lat2 - lat1) * (3.141592 / 180)
    dlon = (lon2 - lon1) * (3.141592 / 180)
    a = (pow(sin(dlat/2), 2) +
         cos(lat1 * (3.141592 / 180)) * cos(lat2 * (3.141592 / 180)) *
         pow(sin(dlon/2), 2))
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = radius * c
    return distance

# 초기화
drive(0, 0)
steer(90)

# 경로 따라가기
while True:
    current_location = get_current_location()
    nearest_point = find_nearest_point(current_location)
    # 현재 위치에서 가장 가까운 경로 점과의 거리와 각도 계산
    distance = get_distance
