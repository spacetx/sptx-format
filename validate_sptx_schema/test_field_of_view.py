import os

from .util import getpaths, load_json, load_validator, validate

SCHEMA_NAME = 'field_of_view'

examples, schema = getpaths()
schema_path = os.path.join(schema, 'field_of_view', f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
validator = load_validator(schema)
examples = os.path.join(examples, SCHEMA_NAME)


def test_field_of_view():
    example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
    example = load_json(example_path)
    assert validate(validator, example)

    # mangle indices
    no_channel = example.copy()
    del no_channel['tiles'][0]['indices']['c']
    assert not validator.is_valid(no_channel)

    # miss-name round
    missnamed_round = example.copy()
    del missnamed_round['tiles'][0]['indices']['r']
    missnamed_round['tiles'][0]['indices']['h'] = 0
    assert not validator.is_valid(missnamed_round)
