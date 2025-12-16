# Mission 1 - Surface Brushing
from hub import port
import runloop
import motor_pair
import motor
import color_sensor
import color
from hub import light_matrix


slowSpeed = 70
normalSpeed = 180
fastSpeed = 320

attachmentUpPosition = 170
attachmentDownPosition = -130


async def main():

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, attachmentUpPosition, normalSpeed)

    motor_pair.move(motor_pair.PAIR_1, 0, velocity=normalSpeed)
    while color_sensor.color(port.B) is not color.GREEN and color_sensor.color(port.F) is not color.GREEN:
        light_matrix.write('Mine Surfers')

    motor_pair.stop(motor_pair.PAIR_1)
    

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, attachmentDownPosition, normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 170, 0, velocity=fastSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

    # Move backward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -300, 0, velocity=fastSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())