import numpy as np
import matplotlib.pyplot as plt
import math

plt.style.use("dark_background")


def _round_decimal_down(number):
    decimal_point_index = str(float(number)).index('.')
    num = str(number)[0:decimal_point_index + 2]
    return float(num)


def _round_decimal_up(number):
    decimal_point_index = str(float(number)).index('.')
    num = str(number)[0:decimal_point_index + 2]
    return round(float(num) + 0.1, 1)


def _fill_thrust_gaps(time_array, thrust_array):
    time = np.array([])
    thrust = np.array([])

    for idx in range(0, len(time_array) - 1):
        x1, y1, x2, y2 = time_array[idx], thrust_array[idx], time_array[idx + 1], thrust_array[idx + 1]
        gradient = (y2 - y2) / (x2 - x1)
        temp_time_array = np.linspace(
            _round_decimal_down(x1),
            _round_decimal_up(x2),
            int((_round_decimal_down(x2) - _round_decimal_up(x1)) * 10 + 1)
        )
        temp_thrust_array = (gradient * temp_time_array) + (y1 - gradient * x1)

        time = np.append(time, temp_time_array)
        thrust = np.append(thrust, temp_thrust_array)

    return time.reshape(1, len(time)), thrust.reshape(1, len(thrust))


class Motor:
    def __init__(self):
        self.time, self.thrust, self.mass_flow_rate, self.mass = None, None, None, None

    def define_with_constant_values(self, total_impulse: float, burn_time: float, total_mass: float,
                                    propellant_mass: float) -> None:

        time = np.round(np.linspace(0, burn_time, int(burn_time / 0.1)), 1)
        time = time.reshape(1, len(time))
        thrust = np.repeat(total_impulse / burn_time, len(time[0]))
        thrust = thrust.reshape(1, len(thrust))
        mass_flow_rate = propellant_mass / burn_time
        mass = total_mass - time * mass_flow_rate

        self.time = np.copy(time)
        self.thrust = np.copy(thrust)
        self.mass_flow_rate = mass_flow_rate
        self.mass = np.copy(mass)

        del time, thrust, mass_flow_rate, mass

    def define_with_variable_values(self, time_array: np.array, thrust_array: np.array, total_mass: float,
                                    propellant_mass: float) -> None:

        time, thrust = _fill_thrust_gaps(time_array, thrust_array)
        mass_flow_rate = propellant_mass / time_array[-1]
        mass = total_mass - time[0] * mass_flow_rate

        self.mass_flow_rate = mass_flow_rate
        self.mass = np.copy(mass)
        self.time = np.copy(time)
        self.thrust = np.copy(thrust)

        del time, thrust, mass_flow_rate, mass

    def plot_thrust_curve(self):
        if self.time is None or self.thrust is None or self.mass_flow_rate is None or self.mass is None:
            print("Define motor parameters with 'define_with_constant_values' or 'define_with_variable_values' method!")
        else:
            plt.plot(self.time[0], self.thrust[0])
            plt.show()
