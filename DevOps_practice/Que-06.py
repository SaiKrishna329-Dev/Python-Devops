# Basic YAML/JSON syntax check

import json
import YAML
import sys
 
def YAML_json_syntax_check(file_path):
    try:
        with open(file_path, r) as f:
            if file_path.endswith(('.yaml', '.yml')):
                yaml.safe_load(f)
            elif file_path.endswith('.json'):
                json.load(f)
            else:
                raise ValueError("File must be .yaml, .yml, or .json")
        print(f"{file_path} is valid syntax")
     except Exception as e:
        print(f" Error in {file_path}: {e}")
        sys.exit(1)

validate_yaml_json("deployment.yaml")


# Schema validation for Kubernetes manifests

import yaml
import sys

REQUIRED_FIELDS = ["apiVersion", "kind", "metadata"]

def validate_k8s_schema(file_path):
    try:
        with open(file_path) as f:
            doc = yaml.safe_load(f)
        for field in REQUIRED_FIELDS:
            if field not in doc:
                raise ValueError(f"Missing required field: {field}")
        print(f"✅ {file_path} passed Kubernetes schema validation")
    except Exception as e:
        print(f"❌ Schema validation failed: {e}")
        sys.exit(1)

validate_k8s_schema("deployment.yaml")