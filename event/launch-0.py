# Launch 0 - Mission 8 - Silo
from hub import port, motion_sensor
import runloop
import motor_pair
import motor

NORMAL_SPEED = 90
FAST_SPEED = 320
ULTRA_FAST_SPEED = 720
START_ATTACHMENT_POSITION = 175
LOWER_ATTACHMENT_POSITION = 10
TURN_SPEED = 150
FIRST_TURN_ANGLE = 45

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

async def right_turn(pair, degrees, speed=TURN_SPEED):
    """
    Turn robot right using gyro (yaw) for a specified degrees
    """
    target_yaw = -degrees * 10# negative for right turn (decidegrees)
    motor_pair.move(pair, 100, velocity=speed)# opposite direction of left turn

    while True:
        yaw, pitch, roll = motion_sensor.tilt_angles()
        print("Yaw (decidegrees):", yaw)
        if yaw <= target_yaw:
            break
        await runloop.sleep_ms(10)

    motor_pair.stop(pair)

async def main():

    # Reset yaw at the very start of mission
    motion_sensor.set_yaw_face(motion_sensor.TOP)
    motion_sensor.reset_yaw(0)

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Bring attachment to starting position
    await motor.run_for_degrees(port.D, START_ATTACHMENT_POSITION, FAST_SPEED)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make first left turn using yaw
    await right_turn(motor_pair.PAIR_1, 45)



    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 270, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make first left turn using yaw
    await left_turn(motor_pair.PAIR_1, -5)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 80, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # # Move the attachment
    # for i in range(5):
    #     await motor.run_for_degrees(port.D, LOWER_ATTACHMENT_POSITION - START_ATTACHMENT_POSITION, ULTRA_FAST_SPEED)
    #     await motor.run_for_degrees(port.D, START_ATTACHMENT_POSITION - LOWER_ATTACHMENT_POSITION, FAST_SPEED)

    # Make first left turn using yaw
    await left_turn(motor_pair.PAIR_1, 45)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 250, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make first left turn using yaw
    await right_turn(motor_pair.PAIR_1, -5)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 230, 0, velocity=FAST_SPEED)
    motor_pair.stop(motor_pair.PAIR_1)

    await motor.run_for_degrees(port.D, -130, FAST_SPEED)

    # Make first left turn using yaw
    await left_turn(motor_pair.PAIR_1, 30)

runloop.run(main())
