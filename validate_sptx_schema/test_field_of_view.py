import os

from .util import getpaths, load_json, load_validator, validate

SCHEMA_NAME = 'field_of_view'

examples, schema = getpaths()
schema_path = os.path.join(schema, 'field_of_view', f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
validator = load_validator(schema)
examples = os.path.join(examples, SCHEMA_NAME)

example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
example = load_json(example_path)


def test_field_of_view():
    assert validate(validator, example)


def test_dartfish_example_field_of_view():
    dartfish_example_path = os.path.join(examples, 'positive', 'dartfish_field_of_view.json')
    dartfish_example = load_json(dartfish_example_path)
    assert validate(validator, dartfish_example)


def test_dartfish_nuclei_example_field_of_view():
    dartfish_nuclei_path = os.path.join(examples, 'positive', 'dartfish_nuclei.json')
    dartfish_nuclei = load_json(dartfish_nuclei_path)
    assert validate(validator, dartfish_nuclei)


def test_channel_must_be_present():
    no_channel = example.copy()
    del no_channel['tiles'][0]['indices']['c']
    assert not validator.is_valid(no_channel)


def test_round_must_be_present():
    misnamed_round = example.copy()
    del misnamed_round['tiles'][0]['indices']['r']
    misnamed_round['tiles'][0]['indices']['h'] = 0
    assert not validator.is_valid(misnamed_round)
