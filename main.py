# IMPORTS
from motor import Motor
from stage import Stage, Booster
from assembly import RocketBody
from simulation import Simulation

# DEFINING COMPONENTS

constant_thrust_test_motor = Motor()
constant_thrust_test_motor.define_with_constant_values(200, 10, 0.05, 0.03)

constant_thrust_test_motor_two = Motor()
constant_thrust_test_motor_two.define_with_constant_values(200, 10, 0.05, 0.03)

test_motor_booster = Booster(
    motor=constant_thrust_test_motor,
    mass=1.0
)

test_motor_booster_two = Booster(
    motor=constant_thrust_test_motor_two,
    mass=1.0
)

# DEFINING BODY

test_stage = Stage(1, test_motor_booster, test_motor_booster_two, 2)
test_stage_two = Stage(2, test_motor_booster)

test_rocket = RocketBody()
test_rocket.add_stage(test_stage, test_stage_two)

# DEFINING SIMULATION

sim = Simulation(test_rocket, 90)
sim.plot_disp_curve()
