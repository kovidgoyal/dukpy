import unittest
from dukpy import Context, undefined


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.ctx = Context()
        self.g = self.ctx.g

    def test_create_context(self):
        pass

    def test_create_new_global_env(self):
        new = self.ctx.new_global_env()

        # The new context should have a distinct global object
        self.g.a = 1
        self.assertIs(new.g.a, undefined)

    def test_eval(self):
        pass

    def test_eval_file(self):
        pass


class ValueTests(unittest.TestCase):
    def setUp(self):
        self.ctx = Context()
        self.g = self.ctx.g

    def test_simple(self):
        for value in [undefined, None, True, False]:
            self.g.value = value
            self.assertIs(self.g.value, value)

        for value in ["foo", 42, 3.141592, 3.141592e20]:
            self.g.value = value
            self.assertEqual(self.g.value, value)

    def test_object(self):
        self.g.value = {}
        self.assertEqual(dict(self.g.value), {})

        self.g.value = {'a': 1}
        self.assertEqual(dict(self.g.value), {'a': 1})

        self.g.value = {'a': {'b': 2}}
        self.assertEqual(dict(self.g.value.a), {'b': 2})

    def test_array(self):
        self.g.value = []
        self.assertEqual(list(self.g.value), [])

        self.g.value = [0, 1, 2]
        self.assertEqual(self.g.value[0], 0)
        self.assertEqual(self.g.value[1], 1)
        self.assertEqual(self.g.value[2], 2)
        self.assertEqual(self.g.value[3], undefined)
        self.assertEqual(list(self.g.value), [0, 1, 2])
        self.assertEqual(len(self.g.value), 3)

        self.g.value[1] = 9
        self.assertEqual(self.g.value[0], 0)
        self.assertEqual(self.g.value[1], 9)
        self.assertEqual(self.g.value[2], 2)
        self.assertEqual(self.g.value[3], undefined)
        self.assertEqual(list(self.g.value), [0, 9, 2])
        self.assertEqual(len(self.g.value), 3)

    def test_callable(self):
        self.g.func = lambda x: x * x
        self.assertEqual(self.g.func(123), 15129)

    def test_proxy(self):
        self.g.obj1 = {'a': 42}
        self.g.obj2 = self.g.obj1
        self.assertEqual(self.g.obj1.a, self.g.obj2.a)
