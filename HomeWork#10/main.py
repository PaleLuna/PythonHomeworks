import coverage


class MealyError(Exception):
    pass


class State:
    def __init__(self, name):
        self.fork_var = None
        self.fork_num = 0

        self.patch_var = None
        self.patch_num = 0

        self.type_var = None
        self.type_num = 0

        self.name = name

    def add_fork(self, state, num):
        self.fork_var = state
        self.fork_num = num

    def add_patch(self, state, num):
        self.patch_var = state
        self.patch_num = num

    def add_type(self, state, num):
        self.type_var = state
        self.type_num = num

    def type(self):
        if self.type_var:
            return self.type_var
        else:
            raise MealyError("type")

    def patch(self):
        if self.patch_var:
            return self.patch_var
        else:
            raise MealyError("patch")

    def fork(self):
        if self.fork_var:
            return self.fork_var
        else:
            raise MealyError("fork")


class Mealy:
    def __init__(self, state):
        self.current_state = state

    def type(self):
        num = self.current_state.type_num
        self.current_state = self.current_state.type()
        return num

    def fork(self):
        num = self.current_state.fork_num
        self.current_state = self.current_state.fork()
        return num

    def patch(self):
        num = self.current_state.patch_num
        self.current_state = self.current_state.patch()
        return num


def make_transition(parent, type_var=None, type_num=0,
                    fork_var=None, fork_num=0, patch_var=0, patch_num=None):
    if type_var is parent:
        type_var.add_type(parent, type_num)
    if fork_var is parent:
        fork_var.add_fork(parent, fork_num)
    if patch_var is parent:
        patch_var.add_patch(parent, patch_num)

    parent.add_type(type_var, type_num)
    parent.add_fork(fork_var, fork_num)
    parent.add_patch(patch_var, patch_num)


def main():
    state_a = State("A")
    state_b = State("B")
    state_c = State("C")
    state_d = State("D")
    state_e = State("E")
    state_f = State("F")

    make_transition(state_a, state_b, 0)
    make_transition(state_b, None, 0, state_c, 1)
    make_transition(state_c, None, 0, state_d, 2, state_c, 3)
    make_transition(state_d, None, 0, None, 0, state_e, 4)
    make_transition(state_e, state_f, 5, state_e, 7, state_a, 6)
    make_transition(state_f, None, 0, None, 0, state_f, 8)

    return Mealy(state_a)


def test():
    m = main()

    assert m.current_state.name == "A"

    assert m.type() == 0
    assert m.fork() == 1
    assert m.patch() == 3
    assert m.fork() == 2
    assert m.patch() == 4
    assert m.fork() == 7
    assert m.patch() == 6

    m1 = main()

    m1.type()
    m1.fork()
    m1.patch()
    m1.fork()
    m1.patch()
    assert m1.type() == 5
    assert m1.patch() == 8

    m2 = main()

    # A state
    try:
        m2.patch()
    except MealyError as e:
        assert str(e) == "patch"
    try:
        m2.fork()
    except MealyError as e:
        assert str(e) == "fork"

    m2.type()

    # B state
    try:
        m2.patch()
    except MealyError as e:
        assert str(e) == "patch"
    try:
        m2.type()
    except MealyError as e:
        assert str(e) == "type"
    m2.fork()

    # C state
    try:
        m2.type()
    except MealyError as e:
        assert str(e) == "type"

    m2.fork()

    # D state
    try:
        m2.fork()
    except MealyError as e:
        assert str(e) == "fork"
    try:
        m2.type()
    except MealyError as e:
        assert str(e) == "type"

    m2.patch()

    m2.type()

    try:
        m2.fork()
    except MealyError as e:
        assert str(e) == "fork"
    try:
        m2.type()
    except MealyError as e:
        assert str(e) == "type"


cov = coverage.Coverage()
cov.start()
test()
cov.stop()
cov.report()
cov.xml_report()
