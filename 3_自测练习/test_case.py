#!/usr/bin/env python3

from my_solution import solution


# 测试用例
def test_solution():
    G = {'a': 'bd', 'b': 'ce', 'c': 'd', 'd': 'ef', 'e': 'f', 'f': ''}
    # 正确答案
    correct_solution = ['a', 'b', 'c', 'd', 'e', 'f']
    
    # 程序求解结果
    result = solution(G)
    assert correct_solution == result
