import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")


def _fill_thrust_gaps(time_array, thrust_array):
    time = np.array([])
    thrust = np.array([])

    temp_time_array = list(range(int(time_array[0] * 10), 1 + int(time_array[-1] * 10)))
    temp_time_array = [i / 10 for i in temp_time_array]
    temp_time_array = np.array(temp_time_array)

    temp_thrust_array = np.interp(temp_time_array, time_array, thrust_array)

    time = np.append(time, temp_time_array)
    thrust = np.append(thrust, temp_thrust_array)

    return time.reshape(1, len(time)), thrust.reshape(1, len(thrust))


class Motor:
    def __init__(self):
        self.time, self.thrust, self.mass_flow_rate, self.mass = None, None, None, None
        self.is_plot_available, self.is_defined = False, False

    def define_with_constant_values(self, total_impulse: float, burn_time: float, total_mass: float,
                                    propellant_mass: float) -> None:

        time = np.round(np.linspace(0, burn_time, int(burn_time / 0.1)), 1)
        time = time.reshape(1, len(time))
        thrust = np.repeat(total_impulse / burn_time, len(time[0]))
        thrust = thrust.reshape(1, len(thrust))
        mass_flow_rate = propellant_mass / burn_time
        mass = total_mass - time[0] * mass_flow_rate
        mass = mass.reshape(1, len(mass))

        self.time = np.copy(time)
        self.thrust = np.copy(thrust)
        self.mass_flow_rate = mass_flow_rate
        self.mass = np.copy(mass)
        self.is_defined = True

        del time, thrust, mass_flow_rate, mass

    def define_with_variable_values(self, time_array: np.array, thrust_array: np.array, total_mass: float,
                                    propellant_mass: float) -> None:

        time, thrust = _fill_thrust_gaps(time_array, thrust_array)
        mass_flow_rate = propellant_mass / time_array[-1]
        mass = total_mass - time[0] * mass_flow_rate
        mass = mass.reshape(1, len(mass))

        self.mass_flow_rate = mass_flow_rate
        self.mass = np.copy(mass)
        self.time = np.copy(time)
        self.thrust = np.copy(thrust)
        self.is_defined = True

        del time, thrust, mass_flow_rate, mass

    def plot_thrust_curve(self):
        if self.is_defined is False:
            print("Define motor parameters with 'define_with_constant_values' or 'define_with_variable_values' method!")
        else:
            plt.plot(self.time[0], self.thrust[0])
            self.is_plot_available = True

    def plot_acceleration_curve(self):
        if self.is_defined is False:
            print("Define motor parameters with 'define_with_constant_values' or 'define_with_variable_values' method!")
        else:
            plt.plot(self.time[0], (self.thrust[0] - self.mass * 9.81) / self.mass)
            self.is_plot_available = True

    def show_plot(self):
        if self.is_defined is False:
            print("Define motor parameters with 'define_with_constant_values' or 'define_with_variable_values' method!")

        if self.is_plot_available is False:
            print("Use 'plot_thrust_curve' or 'plot_acceleration_curve' to generate plot data first!")
        else:
            plt.show()
            self.is_plot_available = False
