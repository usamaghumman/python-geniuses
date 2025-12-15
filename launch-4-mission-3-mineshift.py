# Mission 3 - Mineshift
from hub import port
import runloop
import motor_pair
import motor

normalSpeed = 180
fastSpeed = 720
attachmentUpPosition = 170


async def main():

    # Bring attachment to up position
    await motor.run_for_degrees(port.D, attachmentUpPosition, normalSpeed)

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 900, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make left turn with 2 motors
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -100, 100, velocity=normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make left turn with 2 motors
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -58, 100, velocity=normalSpeed)

    # Bring attachment to down position
    await motor.run_for_degrees(port.D, attachmentUpPosition * -1, normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 820, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

    # Bring attachment to mid position
    await motor.run_for_degrees(port.D, attachmentUpPosition, normalSpeed)

    # Bring attachment to down position
    await motor.run_for_degrees(port.D, attachmentUpPosition * -1, normalSpeed)

    # Make left turn with 2 motors
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -40, 100, velocity=normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 400, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make left turn with 2 motors
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -90, 100, velocity=normalSpeed)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 800, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())