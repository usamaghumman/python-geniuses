# Mission 3 - Mineshift with Yaw-Based Left Turns
from hub import port, motion_sensor
import runloop
import motor_pair
import motor

NORMAL_SPEED = 180
ATTACHMENT_UP_POSITION = 170
TURN_SPEED = 80
FIRST_TURN_ANGLE = 50
SECOND_TURN_ANGLE = 85
THIRD_TURN_ANGLE = 108
FOURTH_TURN_ANGLE = 170



async def left_turn(pair, degrees, speed=TURN_SPEED):
    """
    Turn robot left using gyro (yaw) for a specified degrees
    """
    target_yaw = degrees * 10# convert degrees to decidegrees
    motor_pair.move(pair, -100, velocity=speed)

    while True:
        yaw, pitch, roll = motion_sensor.tilt_angles()
        print("Yaw (decidegrees):", yaw)
        if yaw >= target_yaw:
            break
        await runloop.sleep_ms(10)

    motor_pair.stop(pair)


async def main():
    # Reset yaw at the very start of mission
    motion_sensor.set_yaw_face(motion_sensor.TOP)
    motion_sensor.reset_yaw(0)

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, ATTACHMENT_UP_POSITION, NORMAL_SPEED)

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 900, 0, velocity=NORMAL_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make first left turn using yaw
    await left_turn(motor_pair.PAIR_1, FIRST_TURN_ANGLE)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 0, velocity=NORMAL_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make second left turn using yaw
    await left_turn(motor_pair.PAIR_1, SECOND_TURN_ANGLE)

    # Bring attachment to down position
    await motor.run_for_degrees(port.D, ATTACHMENT_UP_POSITION * -1, NORMAL_SPEED)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 800, 0, velocity=NORMAL_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Bring attachment to mid position
    await motor.run_for_degrees(port.D, ATTACHMENT_UP_POSITION, NORMAL_SPEED)

    # Bring attachment to down position
    await motor.run_for_degrees(port.D, ATTACHMENT_UP_POSITION * -1, NORMAL_SPEED)

    # Make third left turn using yaw
    await left_turn(motor_pair.PAIR_1, THIRD_TURN_ANGLE)

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, ATTACHMENT_UP_POSITION, NORMAL_SPEED)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 800, 0, velocity=NORMAL_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make fourth left turn using yaw
    await left_turn(motor_pair.PAIR_1, FOURTH_TURN_ANGLE)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 500, 0, velocity=NORMAL_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)


runloop.run(main())