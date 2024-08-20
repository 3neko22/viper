import os
import sys, time
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['CODEX_QUANTIZED'] = '1'
os.environ['LOAD_MODELS'] = '0'
os.environ['DATASET'] = 'refcoco'
os.environ['EXEC_MODE'] = 'codex'
script_dir = os.path.abspath('/gaueko0/users/eamor002/viper')
sys.path.append(script_dir)
# from src.main_simple_lib import *

# my_dataset = datasets.get_dataset(config.dataset)
# query = my_dataset.__getitem__(0)['query']
# #show_single_image(img)
# code = get_code(query)
# print(code)

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
access_token = "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"

quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.3", max_length=15000, device_map="auto", token = access_token)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = 'left'
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.3", 
    quantization_config = quantization_config,
    token = access_token)

# # # modelo = torch.nn.parallel(model, device_ids=[0,1],dim=0)
start = time.time()
query = 'Tell me something about Julio Cesar, Roman Dictator'
input_ids = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
input_ids = input_ids["input_ids"].to("cuda")
generated_ids = model.generate(input_ids, max_new_tokens=128)
generated_ids = generated_ids[:, input_ids.shape[-1]:]
generated_text = [tokenizer.decode(gen_id, skip_special_tokens=False) for gen_id in generated_ids]
generated_text = [text.split('\n\n')[0] for text in generated_text]
end = time.time() - start
print(generated_text)
print(end)

# if torch.cuda.device_count() > 1:
#   print("Let's use", torch.cuda.device_count(), "GPUs!")
#   # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
#   model = torch.nn.DataParallel(model)

# print(model.to("cuda"))