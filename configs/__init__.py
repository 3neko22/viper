import os
from omegaconf import OmegaConf

# The default
config_names = os.getenv('CONFIG_NAMES', None) # En vez del None pondriamos  -> (config_codellama, my_config) por ejemplo
if config_names is None:
    config_names = 'Quantized_config'  # Modify this if you want to use another default config

configs = [OmegaConf.load('configs/base_config.yaml')]

if config_names is not None:
    for config_name in config_names.split(','):
        configs.append(OmegaConf.load(f'configs/{config_name.strip()}.yaml'))

# unsafe_merge makes the individual configs unusable, but it is faster
config = OmegaConf.unsafe_merge(*configs)

