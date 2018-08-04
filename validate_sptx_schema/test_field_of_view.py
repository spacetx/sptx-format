import os

from jsonschema import validate, ValidationError
import pytest

from .util import getpaths, load_json

SCHEMA_NAME = 'field_of_view'

examples, schema = getpaths()
schema_path = os.path.join(schema, f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
examples = os.path.join(examples, SCHEMA_NAME)


def test_field_of_view():
    example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
    example = load_json(example_path)
    validate(example, schema)
