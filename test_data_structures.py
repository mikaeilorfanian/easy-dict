import pytest

from easy_dict import EasyAccessDict, EasyDictError


class TestEasyAccessDict(object):
    def test_accessing_keys_by_dot_notation(self):
        regular_dict = {'a': 1}
        easy_dict = EasyAccessDict(regular_dict)
        assert regular_dict['a'] == easy_dict.a

    def test_accessing_non_existing_key_by_dot_notation(self):
        regular_dict = {'a': 1}
        easy_dict = EasyAccessDict(regular_dict)

        with pytest.raises(EasyDictError) as e:
            easy_dict.b
            assert '"b"' in e

    def test_accessing_by_dot_notation_for_nested_structures(self):
        regular_dict = {'a': 1, 'b': {'c': 2}}
        easy_dict = EasyAccessDict(regular_dict)

        assert regular_dict['a'] == easy_dict.a
        assert regular_dict['b']['c'] == easy_dict.b.c

        with pytest.raises(EasyDictError) as e:
            easy_dict.b.d
            assert '"d"' in e
        with pytest.raises(AttributeError):
            easy_dict.b.c.d

    def test_accessing_first_element_in_list_in_nested_structures(self):
        regular_dict = {'a': 1, 'b': {'e': 1, 'c': [{'d': 2}]}}
        easy_dict = EasyAccessDict(regular_dict)

        assert regular_dict['a'] == easy_dict.a
        assert regular_dict['b']['e'] == easy_dict.b.e

        with pytest.raises(EasyDictError) as e:
            easy_dict.b.d
            assert '"d"' in e

        with pytest.raises(TypeError):
            easy_dict.b.c.d

        assert regular_dict['b']['c'][0]['d'] == easy_dict.b.c.first.d

        with pytest.raises(AttributeError):
            easy_dict.a.first

        with pytest.raises(EasyDictError):
            easy_dict.b.first
            assert '"first"' in e

    def test_using_get_method_when_dot_notation_doesnt_work(self):
        regular_dict = {1: '1'}
        easy_dict = EasyAccessDict(regular_dict)
        assert regular_dict[1] == easy_dict.get(1)
        assert easy_dict.get(2, default=2) == 2

        regular_dict = {'a': 1, 'b': {'e': 1, 'c': [{'d': 2}]}}
        easy_dict = EasyAccessDict(regular_dict, make_copy=False)
        assert easy_dict.get('b') == easy_dict.b
        assert easy_dict.get('b').get('c') == easy_dict.b.c

    def test_features_work_properly_when_make_copy_is_False(self):
        regular_dict = {'a': 1, 'b': {'e': 1, 'c': [{'d': 2}]}}
        easy_dict = EasyAccessDict(regular_dict, make_copy=False)

        assert regular_dict['a'] == easy_dict.a
        assert regular_dict['b']['e'] == easy_dict.b.e

        with pytest.raises(EasyDictError) as e:
            easy_dict.b.d
            assert '"d"' in e

        with pytest.raises(TypeError):
            easy_dict.b.c.d

        assert regular_dict['b']['c'][0]['d'] == easy_dict.b.c.first.d

        with pytest.raises(AttributeError):
            easy_dict.a.first

        with pytest.raises(EasyDictError):
            easy_dict.b.first
            assert '"first"' in e

    def test_assigning_value_to_keys(self):
        regular_dict = {'a': 1}
        easy_dict = EasyAccessDict(regular_dict)
        easy_dict.a = 2
        assert easy_dict.a == 2

        regular_dict = {'a': 1, 'b': {'c': 2}}
        easy_dict = EasyAccessDict(regular_dict)
        easy_dict.b.c = 3
        with pytest.raises(AssertionError):
            assert easy_dict.b.c == 3

    def test_iteration(self):
        regular_dict = {'a': 1}
        easy_dict = EasyAccessDict(regular_dict)
        assert [e for e in easy_dict] == ['a']

        regular_dict = {'a': 1, 'b': {'c': 2}}
        easy_dict = EasyAccessDict(regular_dict)
        assert [e for e in easy_dict] == ['a', 'b']
        assert [e for e in easy_dict.b] == ['c']

        regular_dict = {'a': 1, 'b': {'e': 1, 'c': [{'d': 2}]}}
        easy_dict = EasyAccessDict(regular_dict, make_copy=False)
        assert [e for e in easy_dict.b.c.first] == ['d']

    def test_string_representation_of_instances(self):
        regular_dict = {'a': 1}
        easy_dict = EasyAccessDict(regular_dict)
        assert repr(easy_dict) == repr(regular_dict)
