from .stage import Stage


class RocketBody:
    def __init__(self):
        self.mass, self.stages, self.is_defined = None, None, False

    def add_stage(self, *args):
        for i, stage in enumerate(args):
            assert type(stage) == Stage, "Parameter {} MUST be of type Stage".format(i + 1)
            assert stage.is_defined is True, "Define core and side boosters in stage {}".format(i + 1)
            assert stage.stage_number is not None, "Define stage number in stage {}".format(i + 1)

        self.stages = [stage for stage in args]

    def add_components(self):
        pass
