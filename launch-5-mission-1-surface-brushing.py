# Mission 1 - Surface Brushing
from hub import port
import runloop
import motor_pair
import motor
import color_sensor
import color
from hub import light_matrix


NORMAL_SPEED = 180
FAST_SPEED = 320
ATTACHMENT_UP_POSITION = 170
ATTACHMENT_DOWN_POSITION = -130


async def main():

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, ATTACHMENT_UP_POSITION, NORMAL_SPEED)

    motor_pair.move(motor_pair.PAIR_1, 0, velocity=NORMAL_SPEED)
    while color_sensor.color(port.B) is not color.GREEN and color_sensor.color(port.F) is not color.GREEN:
        light_matrix.write('Mine Surfers')

    motor_pair.stop(motor_pair.PAIR_1)
    

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, ATTACHMENT_DOWN_POSITION, NORMAL_SPEED)
    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 170, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Move backward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -300, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())