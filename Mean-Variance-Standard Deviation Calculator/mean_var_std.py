# Mean-Variance-Standard Deviation Calculator
# see Mean-Variance-Standard Deviation Calculator.txt

import numpy as np


def calculate(list):
    if len(list) < 9:
        #print("nine elements are required in the list")
        raise ValueError('List must contain nine numbers.')
    else:
        calculations = {'mean': '', 'variance': '',
                        'standard deviation': '', 'max': '', 'min': '', 'sum': ''}
        # converting list to np array
        input = np.array([list[0:3], list[3:6], list[6:9]])
        print(input)
        calculations.update(
            {'mean': [input.mean(0).tolist(), input.mean(1).tolist(), input.mean().tolist()]})
        calculations.update({'variance': [input.var(
            0).tolist(), input.var(1).tolist(), input.var().tolist()]})
        calculations.update({'standard deviation': [input.std(
            0).tolist(), input.std(1).tolist(), input.std().tolist()]})
        calculations.update(
            {'max': [input.max(0).tolist(), input.max(1).tolist(), input.max().tolist()]})
        calculations.update(
            {'min': [input.min(0).tolist(), input.min(1).tolist(), input.min().tolist()]})
        calculations.update(
            {'sum': [input.sum(0).tolist(), input.sum(1).tolist(), input.sum().tolist()]})

        return calculations


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
