# Mission 7 - Heavy Lifting
from hub import port
import runloop
import motor_pair
import motor

normalSpeed = 180
fastSpeed = 720
attachmentUpPosition = 270
attachmentDownPosition = 170


async def main():

    # Bring attachment to up position
    await motor.run_to_absolute_position(port.D, attachmentUpPosition, normalSpeed)

    # Make a right turn
    await motor.run_for_degrees(port.A, -170, normalSpeed)

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 660, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make a left turn
    await motor.run_for_degrees(port.A, 130, normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 380, 0, velocity=180)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make a left turn
    await motor.run_for_degrees(port.A, 65, normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 230, 0, velocity=180)
    motor_pair.stop(motor_pair.PAIR_1)

    # Bring attachment to down position
    await motor.run_to_absolute_position(port.D, attachmentDownPosition, normalSpeed)

    # Make left turn with 2 motors
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 50, -100, velocity=normalSpeed)

    # Bring attachment to up position
    await motor.run_to_absolute_position(port.D, attachmentUpPosition, normalSpeed)

    # Make right turn with 2 motors
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 60, 100, velocity=normalSpeed)

runloop.run(main())