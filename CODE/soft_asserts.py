class SoftAssert:
    def __init__(self):
        self.errors = []

    def soft_assert(self, condition, msg):
        if not condition:
            self.errors.append(msg)

    def assert_all(self):
        assert not self.errors, f"Soft asserts failed:\n" + "\n".join(self.errors)
