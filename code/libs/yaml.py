import yaml

# safe load yaml file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    
# dictionary to yaml
def dict_to_yaml_text(dict):
    return yaml.dump(dict)