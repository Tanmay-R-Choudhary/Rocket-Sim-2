import numpy as np
import matplotlib.pyplot as plt
from functions import *

'''
class Simulation:
    def __init__(self, rocket, launch_angle):
        self.stage_acceleration_list = []
        self.stage_thrust_list = []
        self.stage_mass_list = []
        self.body = rocket
        self.g = -9.81
        self.launch_angle = launch_angle

        for stage in self.body.stages:
            _temp_core_stage_thrust = np.copy(stage.core_stage.motor.thrust)[0]
            if stage.side_booster is not None:
                _temp_side_stage_thrust = stage.num_side_boosters * np.copy(stage.side_booster.motor.thrust)[0]
                _common_thrust = [sum(common_val) for common_val in zip(_temp_core_stage_thrust, _temp_side_stage_thrust)]
                self.stage_thrust_list.append(
                    np.append(_common_thrust, _temp_core_stage_thrust[len(_temp_side_stage_thrust) - 1:]))
            else:
                self.stage_thrust_list.append(_temp_core_stage_thrust)

        for stage in self.body.stages:
            _temp_core_stage_mass = np.copy(stage.core_stage.motor.mass)[0]
            if stage.side_booster is not None:
                _temp_side_stage_mass = stage.num_side_boosters * np.copy(stage.side_booster.motor.mass)[0]
                _common_mass = [sum(common_val) for common_val in zip(_temp_core_stage_mass, _temp_side_stage_mass)]
                self.stage_mass_list.append(
                    np.append(_common_mass,
                              _temp_core_stage_mass[
                              len(_temp_side_stage_mass) - 1:]) + stage.core_stage.mass + stage.num_side_boosters * stage.side_booster.mass
                )
            else:
                self.stage_mass_list.append(_temp_core_stage_mass)

        total_len, time_array = 0, []
        for stage in self.stage_thrust_list:
            total_len += len(stage)
        for i in range(0, total_len):
            time_array.append(i/10)

        self.time_array = np.array(time_array)

        for i in range(len(self.stage_mass_list)):
            self.stage_acceleration_list.append(self.stage_thrust_list[i] / self.stage_mass_list[i])

    def plot_acceleration_curve(self, stage_number=None):
        if stage_number is None:
            for i, data in enumerate(self.stage_acceleration_list):
                plt.figure("Stage {}".format(i + 1))
                plt.plot(data)
        else:
            plt.plot(self.stage_acceleration_list[stage_number-1])

        plt.show()

    def plot_velocity_curve(self, stage_number=None):
        if stage_number is None:
            for i, data in enumerate(self.stage_acceleration_list):
                plt.figure("Stage {}".format(i + 1))
                plt.plot(integrate_graph([i/10 for i in range(0, len(data))], data))

        plt.show()
'''

class Simulation:
    def __init__(self, rocket, launch_angle):
        self.body = rocket
        self.stage_thrust_array = []
        self.stage_mass_array = []

        for stage in self.body.stages:
            print(stage.stage_number)
            if stage.side_booster is not None:
                temp_total_thrust = np.zeros((1, stage.core_stage.motor.thrust.shape[1]))
                temp_core_thrust, temp_side_thrust = np.copy(stage.core_stage.motor.thrust), np.copy(stage.side_booster.motor.thrust)
                temp_side_thrust = np.append(temp_side_thrust, np.zeros((1, temp_core_thrust.shape[1] - temp_side_thrust.shape[1])))
                temp_side_thrust *= stage.num_side_boosters
                temp_total_thrust += temp_core_thrust + temp_side_thrust
                self.stage_thrust_array.append(temp_total_thrust)

                temp_total_mass = np.zeros((1, len(temp_total_thrust[0])))
                temp_core_mass, temp_side_mass = np.copy(stage.core_stage.motor.mass), np.copy(stage.side_booster.motor.mass)
                temp_core_mass = np.append(temp_core_mass, np.zeros((1, temp_total_mass.shape[1] - temp_core_mass.shape[1])))
                temp_side_mass = np.append(temp_side_mass, np.zeros((1, temp_total_mass.shape[1] - temp_side_mass.shape[1])))
                temp_side_mass *= stage.num_side_boosters
                temp_total_mass += temp_core_mass + temp_side_mass + stage.core_stage.mass + stage.side_booster.mass * stage.num_side_boosters
                self.stage_mass_array.append(temp_total_mass)
            else:
                self.stage_thrust_array.append(np.copy(stage.core_stage.motor.thrust))
                self.stage_mass_array.append(np.copy(stage.core_stage.motor.mass + stage.core_stage.mass))
