import json
import os
from typing import Dict, Tuple
from jsonschema import RefResolver, Draft4Validator
import warnings

dir_path = os.path.dirname(os.path.realpath(__file__))
package_root, _ = os.path.split(dir_path.rstrip('/'))


def getpaths() -> Tuple[str, str]:
    examples = os.path.join(package_root, 'examples')
    schema = os.path.join(package_root, 'schema')
    return examples, schema


def load_validator(schema):
    base_uri = 'file://' + package_root + '/'
    resolver = RefResolver(base_uri, schema)
    validator = Draft4Validator(schema, resolver=resolver)

    return validator


def recurse_through_errors(es, level=0):
    """Recurse through errors posting message
    and schema path until context is empty"""
    # Assuming blank context is a sufficient escape clause here.
    for e in es:
        warnings.warn(
            "***"*level + "subschema level " + str(level) + "\t".join([e.message,
            "Path to error:" + str(e.absolute_schema_path)]) + "\n")
        if e.context:
            level += 1
            recurse_through_errors(e.context, level = level)


def validate(validator, instance):
    """Validate an instance of a schema and report errors."""
    if validator.is_valid(instance):
        return True
    else:
        es = validator.iter_errors(instance)
        recurse_through_errors(es)
        return False


def load_json(json_file: str) -> Dict:
    with open(json_file, 'rb') as f:
        return json.load(f)
