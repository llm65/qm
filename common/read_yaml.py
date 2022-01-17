import yaml


def read_yaml(file):
    with open(file, encoding='utf-8') as f:
        config_info = yaml.load(f, Loader=yaml.SafeLoader)
        return config_info
