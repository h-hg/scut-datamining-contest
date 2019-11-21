# -*- coding: utf-8 -*-
import csv
import uchars
import jieba
userdict_path = 'process/jieba/userdict.txt'
stopwords_path = 'process/jieba/stopwords.txt'

def remove_duplication_userdict():
    global userdict_path
    with open(userdict_path, mode='r',encoding='utf-8') as f:
        data = [line.strip() for line in f.readlines()]
    data = uchars.remove_duplication(data)
    with open(userdict_path, mode='w',encoding='utf-8') as f:
        for string in data:
            f.write(string)
            f.write('\n')

def read_data(input_path, delimiter, output_paths):
    data = []
    with open(input_path, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f,delimiter=delimiter)
        header_r = next(reader) # skip the header
        data = [line for line in reader]
    for i in range(len(output_paths)):
        with open(output_paths[i], mode='w',encoding='utf-8') as f:
            for line in data:
                f.write(line[i])
                f.write('\n')

def remove(input_path, output_path):
    with open(input_path, mode='r',encoding='utf-8') as f1:
        data = [line.strip() for line in f1.readlines()]
        data = uchars.remove(data, lambda uchar: uchars.is_alpha(uchar) or uchars.is_chinese_char(uchar) or uchars.is_chinese_punctuation(uchar) or uchars.is_digist(uchar) or uchars.is_space(uchar))
        with open(output_path, mode='w',encoding='utf-8') as f2:
            for string in data:
                f2.write(string)
                f2.write('\n')

def word_segment(input_path, output_path):
    global stopwords_path, userdict_path

    with open(stopwords_path, mode='r',encoding='utf-8') as f:
        stopWords = [line.strip() for line in f.readlines()]
    # space
    stopWords += [' ', '', None]

    with open(input_path, mode='r',encoding='utf-8') as f:
        data = [line.strip() for line in f.readlines()]

    with open(output_path, mode='w',encoding='utf-8', newline='') as f:
        jieba.load_userdict(userdict_path)
        
        writer = csv.writer(f,delimiter=',')
        for string in data:
            words = jieba.lcut(string)
            words = [w for w in words if w not in stopWords]
        
            writer.writerow(words)

def load_word_segment(input_path):
    with open(input_path, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        return [line for line in reader]
    return None

def val_to_cnt(vals):
    val2cnt = {}
    for val in vals:
        if val in val2cnt:
            val2cnt[val] += 1
        else:
            val2cnt[val] = 1
    return val2cnt

def word_frequency(input_path, output_path):
    words = []
    for line in load_word_segment(input_path):
        words += line
    
    val2cnt = val_to_cnt(words)
    
    # sort by count
    val_cnt = sorted(val2cnt.items(), key =lambda pair:pair[1], reverse=True)

    with open(output_path, mode='w',encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(val_cnt)

if __name__ == "__main__":
    # read_data('offical/test_new.csv', ',', ['process/test_id.txt', 'process/test_data.txt'])    
    # read_data('offical/train.csv', '\t', ['process/train_labels.txt', 'process/train_data.txt']) 
    # remove('process/train_data.txt','process/train_data_remove.txt')
    # remove('process/test_data.txt','process/test_data_remove.txt')
    word_segment('process/train_data_remove_spell.txt','process/train_data_remove_spell_words.csv')
    word_segment('process/test_data_remove_spell.txt','process/test_data_remove_spell_words.csv')
    word_frequency('process/train_data_remove_spell_words.csv', 'process/train_word_frequency.csv')
    word_frequency('process/test_data_remove_spell_words.csv', 'process/test_word_frequency.csv')