import os

from jsonschema import validate, ValidationError
import pytest

from .util import getpaths, load_json

SCHEMA_NAME = 'fov_manifest'

examples, schema = getpaths()
schema_path = os.path.join(schema, f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
examples = os.path.join(examples, SCHEMA_NAME)


def test_fov_manifest():
    example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
    example = load_json(example_path)
    validate(example, schema)


def test_empty_manifest_raises_validation_error():
    example_path = os.path.join(examples, 'negative', 'empty_manifest.json')
    example = load_json(example_path)
    with pytest.raises(ValidationError):
        validate(example, schema)
