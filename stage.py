from motor import Motor


class Booster:
    def __init__(self, motor, mass):
        assert type(motor) == Motor, "The parameter motor MUST be of type Motor"
        assert motor.is_defined is True, "Define motor values with define_motor functions before adding motor to " \
                                         "Booster "
        self.motor = motor
        assert type(mass) == float, "Mass must be a float and in kilograms"
        self.mass = mass
        self.is_defined = True


class Stage:
    def __init__(self, stage_number, core_booster, side_booster=None, num_side_booster=None):
        assert type(core_booster) == Booster, "The parameter core_booster MUST be of type Booster"
        assert core_booster.is_defined is True, "Define booster mass and motor"

        self.core_stage = core_booster
        self.side_booster = side_booster
        self.num_side_boosters = num_side_booster
        self.stage_number = stage_number
        self.is_defined = True
