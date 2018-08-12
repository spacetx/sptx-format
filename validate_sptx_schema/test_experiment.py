import os

from .util import getpaths, load_json, load_validator, validate

SCHEMA_NAME = 'experiment'

examples, schema = getpaths()
schema_path = os.path.join(schema, f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
validator = load_validator(schema)
examples = os.path.join(examples, SCHEMA_NAME)
example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
example = load_json(example_path)


def test_fov():
    assert validate(validator, example)


def test_nuclei_must_be_present():
    wrong_nuclei = example.copy()
    wrong_nuclei['auxiliary_images'] = {'not_nuclei': 'nuclei.json'}
    assert not validator.is_valid(wrong_nuclei, schema)


def test_version_must_be_semantic():
    wrong_version = example.copy()
    wrong_version['version'] = '10a'
    assert not validator.is_valid(wrong_version, schema)


def test_dartfish_example_experiment():
    dartfish_example_path = os.path.join(examples, 'positive', 'dartfish_experiment.json')
    dartfish_example = load_json(dartfish_example_path)
    assert validate(validator, dartfish_example)

