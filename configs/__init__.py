import os
from omegaconf import OmegaConf
import sys

''' 
    To select config file set "CONFIG_NAMES" environment variable with the name of the file

    Examples: 
        - setenv CONFIG_NAMES "base_config"  
        - senenv CONFIG_NAMES "base_config, my_config, ..." -> To select multiple files
'''

# The default -> para cambiar 
config_names = os.getenv('CONFIG_NAMES', None) # En vez del None pondriamos  -> (config_codellama, my_config) por ejemplo
enable_models = bool(int(os.getenv('LOAD_MODELS', '0')))
if config_names is not None:
    print("SELECTED CONFIG FILES: " + config_names)
if config_names is None:
    config_names = 'config_codellama_Q'  # Modify this if you want to use another default config

if enable_models:
    configs = [OmegaConf.load('configs/base_config.yaml')]
    print("LOADING MODEL: ENABLED")
else:
    configs = [OmegaConf.load('configs/disable_models.yaml')]
    print("LOADING MODEL: DISABLED")

if config_names is not None:
    for config_name in config_names.split(','):
        configs.append(OmegaConf.load(f'configs/{config_name.strip()}.yaml')) 

# unsafe_merge makes the individual configs unusable, but it is faster
config = OmegaConf.unsafe_merge(*configs)

