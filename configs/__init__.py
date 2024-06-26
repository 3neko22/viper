import os
from omegaconf import OmegaConf
import sys
import yaml

''' 
    To select config file set "CONFIG_NAMES" environment variable with the name of the file

    Examples: 
        - setenv CONFIG_NAMES "base_config"  
        - senenv CONFIG_NAMES "base_config, my_config, ..." -> To select multiple files
'''

# The default -> para cambiar 
isquantized = bool(int(os.getenv('CODEX_QUANTIZED', '0')))

if isquantized:
    dataset_name = os.getenv('DATASET', None)
    execution_mode = os.getenv('EXEC_MODE', None) # En vez del None pondriamos  -> (config_codellama, my_config) por ejemplo
    enable_models = bool(int(os.getenv('LOAD_MODELS', '0')))
    cognition_models = os.getenv('COGNITION_MODEL', None) # config_mistral or config_gemma
    config_names = []
    if enable_models:
        print("LOADING MODEL: ENABLED")
    try:
        if dataset_name in ['refcoco','gqa', 'okvqa']:
            config_names.append(dataset_name + '/'+ 'general_config')
            if execution_mode is not None:
                if execution_mode == 'cache':
                    config_names.append(dataset_name + '/'+ 'execute_with_cache')
                    if cognition_models is not None:
                        config_names.insert(0, cognition_models)
                    else:
                        config_names.insert(0,'config_codellama_Q')
                elif execution_mode == 'codex':
                    config_names.insert(0,'config_codellama_Q')
                    config_names.append(dataset_name + '/'+ 'save_codex')
                elif not execution_mode in [None, 'cache', 'codex']:
                    raise NameError(f'Value from $EXEC_MODE variable is incorrect, obtained: {execution_mode} and must be: cache or codex')
            config_names_=','.join(config_names)
            config_names = config_names_
        else: 
            raise UserWarning(f"There is not any dataset setted or obtained value ({dataset_name}) from '$DATASET' ENV $variable is INCORRECT")
    except NameError as n:
        print(f'ERROR: {n}')
        exit()
    except UserWarning as w:
        print(f'WARNING !!!!: {w}')

    if dataset_name is None:
        config_names = 'config_codellama_Q'  # Modify this if you want to use another default config

    print("SELECTED CONFIG FILES: " + config_names) 
    configs = [OmegaConf.load('configs/base_config.yaml')]
    
    if config_names is not None:
        for config_name in config_names.split(','):
            configs.append(OmegaConf.load(f'configs/project_configs/{config_name.strip()}.yaml'))
        
    if not enable_models: 
        print("LOADING MODEL: DISABLED")
        configs.append(OmegaConf.load(f'configs/project_configs/disable_models.yaml'))

else: # Code for the original project
    # The default
    config_names = os.getenv('CONFIG_NAMES', None)
    if config_names is None:
        config_names = 'my_config'  # Modify this if you want to use another default config

    configs = [OmegaConf.load('configs/base_config.yaml')]

    if config_names is not None:
        for config_name in config_names.split(','):
            configs.append(OmegaConf.load(f'configs/{config_name.strip()}.yaml'))

# unsafe_merge makes the individual configs unusable, but it is faster
config = OmegaConf.unsafe_merge(*configs)