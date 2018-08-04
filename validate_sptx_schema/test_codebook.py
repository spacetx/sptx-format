import os

import pytest
from jsonschema import validate, ValidationError

from .util import getpaths, load_json

examples, schema = getpaths()
codebook_schema_path = os.path.join(schema, 'codebook.json')
codebook_schema = load_json(codebook_schema_path)
examples = os.path.join(examples, 'codebook')


def test_codebook():
    codebook_example_path = os.path.join(examples, 'positive', 'codebook.json')
    codebook_example = load_json(codebook_example_path)
    validate(codebook_example, codebook_schema)


def test_diagonal_codebook():
    codebook_example_path = os.path.join(examples, 'positive', 'codebook_diagonal.json')
    codebook_example = load_json(codebook_example_path)
    validate(codebook_example, codebook_schema)


def test_diagonal_codebook_full_values():
    codebook_example_path = os.path.join(
        examples, 'positive', 'codebook_diagonal_inferred_value.json')
    codebook_example = load_json(codebook_example_path)
    validate(codebook_example, codebook_schema)


def test_codebook_missing_channel_raises_validation_error():
    codebook_example_path = os.path.join(
        examples, 'negative', 'codebook_missing_channel.json')
    codebook_example = load_json(codebook_example_path)
    with pytest.raises(ValidationError):
        validate(codebook_example, codebook_schema)

