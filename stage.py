from .motor import Motor


class Booster:
    def __init__(self):
        self.motor, self.mass, self.is_defined = None, None, False

    def add_motor(self, motor):
        assert type(motor) == Motor, "The parameter motor MUST be of type Motor"
        assert motor.is_defined is True, "Define motor values with define_motor functions before adding motor to Booster"

        self.motor = motor

        if self.mass is not None:
            self.is_defined = True

    def define_booster_dry_mass(self, mass):
        assert type(mass) == float, "Mass must be a float and in kilograms"

        self.mass = mass

        if self.motor is not None:
            self.is_defined = True


class Stage:
    def __init__(self):
        self.core_stage, self.side_boosters = None, None

    def add_core_stage(self, core_booster):
        assert type(core_booster) == Booster, "The parameter core_booster MUST be of type Booster"
        assert core_booster.is_defined is True, "Define booster mass and motor"

        self.core_stage = core_booster

    def add_side_boosters(self, *args):
        for booster in args:
            assert type(booster) == Booster, "The parameter side booster list MUST have items of type Booster"
            assert booster.is_defined is True, "Define all side boosters completely"

        self.side_boosters = [booster for booster in args]
