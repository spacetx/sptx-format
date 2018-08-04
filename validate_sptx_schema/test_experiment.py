import os

from jsonschema import validate, ValidationError
import pytest

from .util import getpaths, load_json

SCHEMA_NAME = 'experiment'

examples, schema = getpaths()
schema_path = os.path.join(schema, f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
examples = os.path.join(examples, SCHEMA_NAME)


def test_fov_with_bad_nuclei_name_throws_error():
    example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
    example = load_json(example_path)
    # correct schema
    validate(example, schema)

    # now, use an incorrect name for the nuclei field and verify an error is thrown
    example['auxiliary_images'] = {'not_nuclei': 'nuclei.json'}
    with pytest.raises(ValidationError):
        validate(example, schema)
