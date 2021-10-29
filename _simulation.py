import numpy as np
import matplotlib.pyplot as plt
from ._functions import *


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
