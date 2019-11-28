# -*- coding: utf-8 -*-
import pickle
def load_data(input_path):
    data = None
    with open(input_path, mode='r', encoding='utf-8') as f:
        data = [line.strip() for line in f.readlines()]
    return data
def write_data(data, out_path):
    with open(out_path, mode='w', encoding='utf-8') as f:
        for line in data:
            f.write(line)
            f.write('\n')

def save_model(file_path, model):
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)

def load_model(file_path):
    model = None
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model    

from aip import AipNlp
app_id      =   'XXXX'
api_key     =   'XXXX'
secret_key  =   'XXXX'

client = AipNlp(app_id, api_key, secret_key)

test_data = load_data('test_data_remove_spell.txt')
train_data = load_data('train_data_remove_spell.txt')

def correct(data, text_out_path, bin_out_path):
    responses = []
    texts = []
    i = 0
    for line in data:
        if i % 100 == 0:
            print(i)
        i += 1
        response = client.ecnet(line)
        responses.append(response)
        texts.append(response['item']['correct_query'])
    write_data(texts, text_out_path)
    save_model(bin_out_path, responses)


correct(test_data, 'test.txt', 'test.bin')