import json
import os
from typing import Dict, Tuple


def getpaths() -> Tuple[str, str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    package_root, _ = os.path.split(dir_path.rstrip('/'))
    examples = os.path.join(package_root, 'examples')
    schema = os.path.join(package_root, 'schema')
    return examples, schema


def load_json(json_file: str) -> Dict:
    with open(json_file, 'rb') as f:
        return json.load(f)
