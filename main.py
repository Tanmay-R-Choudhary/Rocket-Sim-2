# IMPORTS
from motor import Motor
from stage import Stage, Booster
from assembly import RocketBody
from simulation import Simulation
import numpy as np
import matplotlib.pyplot as plt

constant_thrust_test_motor = Motor()
constant_thrust_test_motor.define_with_constant_values(100, 10, 0.05, 0.03)

constant_thrust_test_motor_two = Motor()
constant_thrust_test_motor_two.define_with_constant_values(100, 10, 0.05, 0.03)

test_motor_booster = Booster(
    motor=constant_thrust_test_motor,
    mass=1.0
)

test_motor_booster_two = Booster(
    motor=constant_thrust_test_motor_two,
    mass=1.0
)

test_stage = Stage(1, test_motor_booster, test_motor_booster_two, 2)
test_stage_two = Stage(2, test_motor_booster)

test_rocket = RocketBody()
test_rocket.add_stage(test_stage, test_stage_two)

sim = Simulation(test_rocket, 90)

print(sim.stage_mass_array)