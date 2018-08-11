import os

from .util import getpaths, load_json, load_validator

SCHEMA_NAME = 'fov_manifest'

examples, schema = getpaths()
schema_path = os.path.join(schema, f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
validator = load_validator(schema)
examples = os.path.join(examples, SCHEMA_NAME)


def test_fov_manifest():
    example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
    example = load_json(example_path)
    assert validator.is_valid(example, schema)


def test_empty_manifest_raises_validation_error():
    example_path = os.path.join(examples, 'negative', 'empty_manifest.json')
    example = load_json(example_path)
    assert not validator.is_valid(example, schema)
