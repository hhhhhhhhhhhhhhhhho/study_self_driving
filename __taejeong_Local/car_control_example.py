import time
import math


class software_control_car:
    #### steering parameter ####
    velocity = 0
    gear = 0 
    car_break = 0 

    throttle1 = 0
    throttle2 = 0

    steering_front_left = 0
    steering_front_right = 0
    steering_behind_left = 0  ### 어차피 뒷바퀴는 0으로 고정 될 것이긴 하지만 인지용으로 둠
    steering_behind_right = 0

    #### sensor parameter ####
    car_position_from_Gps_x = 0
    car_position_from_Gps_y = 0

    #### car body status ####
    yaw_rate = 0
    motor_rate = 0

    ### 규정에 맞는 소프트웨어 모드 적용 
    control_mode = 0 
    
    def __init__(self, compete_mode, control_mode):

        self.velocity = 0
    
        self.gear = 0
        self.car_break = 0

        self.steering_behind_left = 0
        self.steering_behind_right = 0
        self.steering_front_left = 0
        self.steering_front_right = 0 

        self.car_position_from_Gps_x = 0
        self.car_position_from_Gps_y = 0

        self.yaw_rate = 0
        self.car_break = 0 

        self.control_mode = control_mode

    def _Set_speed(speed):
        ####보완필요 : 모터와 실제 속도간의 관계 정의 필요함
        ####보완필요 : 축에 가까운 바퀴가 덜움직이는데 이것도 정의 필요 함. 
        return 

    def _Set_throttle(self,left_speed,right_speed):
        self.throttle1 = self.set_speed(left_speed)
        self.throttle2 = self.set_speed(right_speed)

    def _Set_steer():
        #### 보완필요 서보모터와 조향각 간의 관계 정의 필요 함. 
        #### 차체길이, 차체무게중심, 전륜 ( 앞바퀴 왼쪽 오른쪽 각도 )
        return 

    def _MODE_AutoDriving(self):
        return
    
    def _MODE_(self):
        return
    
    def _MODE_(self):
        return 
        





        


