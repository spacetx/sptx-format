import os

from .util import getpaths, load_json, load_validator

SCHEMA_NAME = 'experiment'

examples, schema = getpaths()
schema_path = os.path.join(schema, f'{SCHEMA_NAME}.json')
schema = load_json(schema_path)
validator = load_validator(schema)
examples = os.path.join(examples, SCHEMA_NAME)


def test_fov_with_bad_nuclei_name_throws_error():
    example_path = os.path.join(examples, 'positive', f'{SCHEMA_NAME}.json')
    example = load_json(example_path)
    # correct schema
    assert validator.is_valid(example, schema)

    # now, use an incorrect name for the nuclei field and verify an error is thrown
    wrong_nuclei = example.copy()
    wrong_nuclei['auxiliary_images'] = {'not_nuclei': 'nuclei.json'}
    assert not validator.is_valid(wrong_nuclei, schema)

    # mangle the version
    wrong_version = example.copy()
    wrong_version['version'] = '10a'
    assert not validator.is_valid(wrong_version, schema)
