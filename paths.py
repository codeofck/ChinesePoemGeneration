#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
This file provides variables which store path to directions and source data.
'''

import os

root_dir = os.path.dirname(__file__)
data_dir = os.path.join(root_dir, 'data')
raw_dir = os.path.join(root_dir, 'raw')
save_dir = os.path.join(root_dir, 'save')

sxhy_path = os.path.join(data_dir, 'sxhy_dict.txt')
word_dict_path = os.path.join(data_dir, 'word_dict_128.txt')
poems_path = os.path.join(data_dir, 'poem_128.txt')
#poems_path = os.path.join(data_dir, 'poem.txt')
word2vec_path = os.path.join(data_dir, 'embedding_128.npy')
wordrank_path = os.path.join(data_dir, 'wordrank.json')
plan_data_path = os.path.join(data_dir, 'plan_data.txt')
gen_data_path = os.path.join(data_dir, 'gen_data.txt')


# TODO: configure dependencies in another file.
_dependency_dict = {
        poems_path : [word_dict_path],
        word2vec_path : [word_dict_path, poems_path],
        wordrank_path : [sxhy_path, poems_path],
        gen_data_path : [word_dict_path, poems_path, sxhy_path, word2vec_path],
        plan_data_path : [word_dict_path, poems_path, sxhy_path, word2vec_path],
        }

def check_uptodate(path: str) -> bool:
    """
    Return true iff the file exists and up-to-date with dependencies.
    """
    return os.path.exists(path)
