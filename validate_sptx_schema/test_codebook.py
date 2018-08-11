import os

from .util import getpaths, load_json, validate, load_validator

examples, schema = getpaths()
codebook_schema_path = os.path.join(schema, 'codebook', 'codebook.json')
codebook_schema = load_json(codebook_schema_path)
validator = load_validator(codebook_schema)
examples = os.path.join(examples, 'codebook')


def test_codebook():
    codebook_example_path = os.path.join(examples, 'positive', 'codebook.json')
    codebook_example = load_json(codebook_example_path)
    assert validate(validator, codebook_example)


def test_diagonal_codebook():
    codebook_example_path = os.path.join(examples, 'positive', 'codebook_diagonal.json')
    codebook_example = load_json(codebook_example_path)
    assert validate(validator, codebook_example)


def test_diagonal_codebook_full_values():
    codebook_example_path = os.path.join(
        examples, 'positive', 'codebook_diagonal_inferred_value.json')
    codebook_example = load_json(codebook_example_path)
    assert validate(validator, codebook_example)


def test_codebook_missing_channel_raises_validation_error():
    codebook_example_path = os.path.join(
        examples, 'negative', 'codebook_missing_channel.json')
    codebook_example = load_json(codebook_example_path)
    assert not validator.is_valid(codebook_example)
