'''
info: --> Auto create header by korofileheader <--
Author: Northern NOOB
Mail: northsnoob@gmail.com
Date: 2024-09-22 00:33
LastEditors: Northern NOOB
LastEditTime: 2024-09-22 01:11
Version: default
'''
import numpy as np
def stonegame(_in):
    stone_length = len(_in)
    path_mask = [0]+[1]*(stone_length-1)
    score = 0
    predict_list = np.zeros(0)
    pivot = 0
    lenlist = np.arange(0,stone_length)
    pivots_log = []
    for i in range(stone_length-1):
        
        predict_list = list_in*np.abs(lenlist-pivot)
        predict_list = predict_list*path_mask
        # print(predict_list)
        # pivot = np.argmax(predict_list)
        pred_sort = np.argsort(predict_list)[::-1]
        # print(pred_sort)
        if predict_list[pred_sort[0]] == predict_list[pred_sort[1]]: # 有bug
            pivot = max(abs(pred_sort[0]-pivot),abs(pred_sort[1]-pivot))+pivot
        else:
            pivot = pred_sort[0]
        # print(pivot)
        path_mask[pivot] = 0
        score += predict_list[pivot]
        pivots_log.append(pivot)
        
    print("pivots:",pivots_log)
    return score


if __name__ == '__main__':
    list_in = np.array([3, 7, 2, 10, 5, 12, 8, 10, 1],dtype=int)
    result = stonegame(list_in)
    print(result)