import numpy as np
import matplotlib.pyplot as plt
from functions import *


class Simulation:
    def __init__(self, rocket, launch_angle, sim_time_after_burnout=500):
        self.body = rocket
        self.stage_thrust_array = []
        self.stage_mass_array = []
        self.g = -9.81

        for stage in self.body.stages:
            if stage.side_booster is not None:
                temp_total_thrust = np.zeros((1, stage.core_stage.motor.thrust.shape[1]))
                temp_core_thrust, temp_side_thrust = np.copy(stage.core_stage.motor.thrust), np.copy(
                    stage.side_booster.motor.thrust)
                temp_side_thrust = np.append(temp_side_thrust,
                                             np.zeros((1, temp_core_thrust.shape[1] - temp_side_thrust.shape[1])))
                temp_side_thrust *= stage.num_side_boosters
                temp_total_thrust += temp_core_thrust + temp_side_thrust
                self.stage_thrust_array.append(temp_total_thrust * np.sin(launch_angle * (np.pi / 180)))

                temp_total_mass = np.zeros((1, len(temp_total_thrust[0])))
                temp_core_mass, temp_side_mass = np.copy(stage.core_stage.motor.mass), np.copy(
                    stage.side_booster.motor.mass)
                temp_core_mass = np.append(temp_core_mass,
                                           np.zeros((1, temp_total_mass.shape[1] - temp_core_mass.shape[1])))
                temp_side_mass = np.append(temp_side_mass,
                                           np.zeros((1, temp_total_mass.shape[1] - temp_side_mass.shape[1])))
                temp_side_mass *= stage.num_side_boosters
                temp_total_mass += temp_core_mass + temp_side_mass + stage.core_stage.mass + stage.side_booster.mass * stage.num_side_boosters
                self.stage_mass_array.append(temp_total_mass)
            else:
                self.stage_thrust_array.append(np.copy(stage.core_stage.motor.thrust) * np.sin(launch_angle * (np.pi / 180)))
                self.stage_mass_array.append(np.copy(stage.core_stage.motor.mass + stage.core_stage.mass))

            time_array_length = 0

            for i in self.stage_thrust_array:
                time_array_length += len(i[0])

            time = [i / 10 for i in range(0, time_array_length + 1 + sim_time_after_burnout)]
            self.sim_time = np.array([time])

            thrust = []
            for thrust_array in self.stage_thrust_array:
                thrust.extend(thrust_array[0])

            extension = [0 for i in range(0, len(self.sim_time[0]) - len(thrust))]
            thrust.extend(extension)

            self.flight_thrust_array = np.array([thrust])

            mass = []
            for mass_array in self.stage_mass_array:
                mass.extend(mass_array[0])

            extension = [mass[-1] for i in range(0, len(self.sim_time[0]) - len(mass))]
            mass.extend(extension)

            self.flight_mass_array = np.array([mass])

            acc = []
            for i, thrust_array in enumerate(self.stage_thrust_array):
                acc.extend(thrust_array[0] / self.stage_mass_array[i][0])

            extension = [0 for i in range(0, len(self.sim_time[0]) - len(acc))]
            acc.extend(extension)

            self.flight_acc_array = np.array([acc]) + self.g

            self.flight_velocity_array = np.array([integrate_graph(self.sim_time[0], self.flight_acc_array[0])])

            self.flight_displacement_array = np.array([integrate_graph(self.sim_time[0], self.flight_velocity_array[0])])

            del extension, mass, thrust, acc, time, time_array_length

    def plot_thrust_curve(self):
        plt.plot(self.sim_time[0], self.flight_thrust_array[0])
        plt.show()

    def plot_mass_curve(self):
        plt.plot(self.sim_time[0], self.flight_mass_array[0])
        plt.show()

    def plot_acc_curve(self):
        plt.plot(self.sim_time[0], self.flight_acc_array[0])
        plt.show()

    def plot_vel_curve(self):
        plt.plot(self.sim_time[0], self.flight_velocity_array[0])
        plt.show()

    def plot_disp_curve(self):
        plt.plot(self.sim_time[0], self.flight_displacement_array[0])
        plt.show()
