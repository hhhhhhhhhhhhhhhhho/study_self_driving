import RPi.GPIO as GPIO
import time

# 핀 번호 할당 방식 설정
GPIO.setmode(GPIO.BOARD)

# 모터 핀 번호 설정
motor1_pin1 = 11
motor1_pin2 = 12
motor2_pin1 = 13
motor2_pin2 = 15

# 서보모터 핀 번호 설정
servo_pin = 22

# 핀 모드 설정
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

# 서보모터 객체 생성
servo = GPIO.PWM(servo_pin, 50)

# 모터 제어 함수
def drive(left_speed, right_speed):
    if left_speed > 0:
        GPIO.output(motor1_pin1, GPIO.HIGH)
        GPIO.output(motor1_pin2, GPIO.LOW)
    elif left_speed < 0:
        GPIO.output(motor1_pin1, GPIO.LOW)
        GPIO.output(motor1_pin2, GPIO.HIGH)
    else:
        GPIO.output(motor1_pin1, GPIO.LOW)
        GPIO.output(motor1_pin2, GPIO.LOW)
    if right_speed > 0:
        GPIO.output(motor2_pin1, GPIO.HIGH)
        GPIO.output(motor2_pin2, GPIO.LOW)
    elif right_speed < 0:
        GPIO.output(motor2_pin1, GPIO.LOW)
        GPIO.output(motor2_pin2, GPIO.HIGH)
    else:
        GPIO.output(motor2_pin1, GPIO.LOW)
        GPIO.output(motor2_pin2, GPIO.LOW)
    # 듀티 사이클 조절
    motor1_speed = abs(left_speed) * 100 / 255
    motor2_speed = abs(right_speed) * 100 / 255
    kit.motor1.throttle = motor1_speed
    kit.motor2.throttle = motor2_speed

# 조향각 제어 함수
def steer(angle):
    duty = angle / 18 + 2.5
    servo.start(duty)
    time.sleep(0.5)
    servo.stop()

# 경로 따라가기
while True:
    # 경로 정보 받아오기
    # 현재 위치 정보 받아오기
    current_location = (37.123, 127.456)  # 예시를 위해 임의의 값 설정
    # 경로에서 현재 위치에서 가장 가까운 점 찾기
    nearest_point = (37.234, 127.567)  # 예시를 위해 임의의 값 설정
    # 현재 위치와 가장 가까운 점 사이의 거리와 각도 계산
    distance = 10  # 예시를 위해 임의의 값 설정
    angle = 30 
