# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:06:04 2018

Author: sdc

E-mail:873892935@qq.com
"""
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    

for row in range(len(grid[0])):
    for line in range(len(grid)):
        print(grid[line][row], end = ' ')
    print()

