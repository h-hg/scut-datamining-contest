# -*- coding: utf-8 -*-

def replace(data, old_str, new_str):
    """
    replace the old_str of string in the data with new_str\\
    return the new data
    """
    # return list(map(lambda str: str.replace(old_str,new_str), data))
    return [str.replace(old_str, new_str) for str in data]


def is_chinese_char(uchar):
    return uchar >= u'\u4e00' and uchar <= u'\u9fa5'

def is_chinese_punctuation(uchar):
    chinese_punctuations = [u'。', u'，', u'、', u'？', u'：', u'、', u'“', u'”', u'！']
    return uchar in chinese_punctuations

def is_digist(uchar):
    return '0' <= uchar and uchar <= '9'
    
def is_alpha(uchar):
    return ('a' <= uchar and uchar <= 'z') or ('A' <= uchar and uchar <= 'Z')

def is_space(uchar):
    return uchar == ' '

def remove(data, pattern):
    """
    remove the char of string in the data, which makes pattern(char) True \\
    return the new data
    """
    return [''.join(filter(pattern, str)) for str in data]

def remove_duplication(data):
    return list(set(data))