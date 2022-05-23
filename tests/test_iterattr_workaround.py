import unittest

from src.script import get_attr_or_iter_from_str_nested


class Object_1():
    def __init__(self):
        self.dictionary = {'name': 'Name'}
        self.nested_dictionary = {'obj_3':
                                  {'name': 'Name',
                                   'type': 'String'}}
        self.array = [234, 234234, 23412345]
        self.integer = 123
        self.string = 'String'


class Object_2():
    def __init__(self):
        self.obj_3 = Object_1()


class WorkaroundScriptTests(unittest.TestCase):
    check = True
    fast = False

    def setUp(self):
        self.obj_4 = Object_2()

    def tearDown(self):
        del(self.obj_4)

    def test_integer(self):
        attr_str = 'obj_3.integer'
        attr = self.obj_4.obj_3.integer
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_string(self):
        attr_str = 'obj_3.string'
        attr = self.obj_4.obj_3.string
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_dictionary(self):
        attr_str = 'obj_3.dictionary'
        attr = self.obj_4.obj_3.dictionary
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_dictionary_element_1(self):
        attr_str = "obj_3.dictionary['name']"
        attr = self.obj_4.obj_3.dictionary['name']
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_dictionary_element_2(self):
        attr_str = 'obj_3.dictionary["name"]'
        attr = self.obj_4.obj_3.dictionary["name"]
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_dictionary_element_3(self):
        attr_str = 'obj_3.dictionary[\'name\']'
        attr = self.obj_4.obj_3.dictionary['name']
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_list_element_1(self):
        attr_str = 'obj_3.array[1]'
        attr = self.obj_4.obj_3.array[1]
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)

    def test_nested_dictionary_element_1(self):
        attr_str = "obj_3.nested_dictionary['obj_3']['name']"
        attr = self.obj_4.obj_3.nested_dictionary['obj_3']['name']
        attr_2 = get_attr_or_iter_from_str_nested(
                self.obj_4, attr_str, check=self.check, fast=self.fast)
        self.assertEqual(attr, attr_2)


class WorkaroundScriptTests_fast(WorkaroundScriptTests):
    fast = True


class WorkaroundScriptTests_no_check(WorkaroundScriptTests):
    check = False


class WorkaroundScriptTests_fast_no_check(WorkaroundScriptTests_fast):
    check = False
