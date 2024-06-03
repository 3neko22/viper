import os
import sys
os.environ['CONFIG_NAMES'] = 'config_codellama_q,benchmarks/refcoco'
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2'
script_dir = os.path.abspath('/gaueko0/users/eamor002/viper')
sys.path.append(script_dir)
from src.main_simple_lib import *
# from main_simple_lib import show_single_image
# from configs import config
# from datasets import get_dataset
#dataset_config = config.dataset

# dataset = get_dataset(dataset_config)

# elementua = dataset.__getitem__(0) # './data/refcoco/mscoco/train2014/COCO_train2014_000000022102.jpg'
# show_single_image(elementua['image'])
#import time

# start = time.time()
# query = 'pizza front'
# code =get_code(query)

# print(code)

# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
# print(torch.cuda.device_count())
# device = torch.device("cuda:0")

# with open('prompts/benchmarks/refcoco.prompt') as f:
#     prompt = f.read().strip()
# p = "Drink with zero alcohol"
# if isinstance(prompt,str):
#     extended_prompt = prompt.replace("INSERT_QUERY_HERE", p)
# #print(extended_prompt)

# quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16, attn_implementation="flash_attention_2")
# tokenizer = AutoTokenizer.from_pretrained('codellama/CodeLlama-7b-hf', max_length=15000, device_map="auto")
# tokenizer.pad_token = tokenizer.eos_token
# tokenizer.padding_side = 'left'
# model = AutoModelForCausalLM.from_pretrained(
#     'codellama/CodeLlama-7b-hf', 
#     quantization_config = quantization_config,
#     max_memory=5000)

# # # modelo = torch.nn.parallel(model, device_ids=[0,1],dim=0)
# start = time.time()
# input_ids = tokenizer(extended_prompt, return_tensors="pt", padding=True, truncation=True)
# input_ids = input_ids["input_ids"].to("cuda")
# generated_ids = model.generate(input_ids, max_new_tokens=128)
# generated_ids = generated_ids[:, input_ids.shape[-1]:]
# generated_text = [tokenizer.decode(gen_id, skip_special_tokens=False) for gen_id in generated_ids]
# generated_text = [text.split('\n\n')[0] for text in generated_text]
# end = time.time() - start
# print(generated_text)
# print(end)

# if torch.cuda.device_count() > 1:
#   print("Let's use", torch.cuda.device_count(), "GPUs!")
#   # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
#   model = torch.nn.DataParallel(model)

# print(model.to("cuda"))