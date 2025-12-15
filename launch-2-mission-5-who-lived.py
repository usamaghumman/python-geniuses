from hub import port
import runloop
import motor_pair
import motor

vel = 180
vel2 = 720

startingAttachmentAngle = 110

async def main():

    # Bring attachment to starting position
    await motor.run_to_absolute_position(port.D, startingAttachmentAngle, vel)

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 870, 0, velocity=vel)

    # Move attachment to left
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 100, -80, velocity=vel2)

    # Add delay before going more left to add more force and settle things down
    await runloop.sleep_ms(500)

    # Move attachment to left
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 100, -80, velocity=vel)

    # Return
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -800, 0, velocity=vel)

    # Stop motor pair
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())