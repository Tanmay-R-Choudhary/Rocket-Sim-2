import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, rocket, launch_angle):
        self.stage_thrust_list = []
        self.body = rocket
        self.g = -9.81
        self.launch_angle = launch_angle

        for stage in self.body.stages:
            _temp_core_stage_thrust = np.copy(stage.core_stage.motor.thrust)[0]
            _temp_side_stage_thrust = stage.num_side_boosters * np.copy(stage.side_booster.motor.thrust)[0]
            _common_thrust = [sum(common_val) for common_val in zip(_temp_core_stage_thrust, _temp_side_stage_thrust)]
            self.stage_thrust_list.append(np.append(_common_thrust, _temp_core_stage_thrust[len(_temp_side_stage_thrust) - 1:]))
