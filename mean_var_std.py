import numpy as np


def calculate(list):
  if (len(list) !=9):
    raise ValueError("List must contain nine numbers.")
  
  ls = np.array(list)
  ls = ls.reshape ((3, 3))
  print(ls)

  mean_rows = [ls[0, :].mean(), ls[1, :].mean(), ls[2, :].mean()]
  mean_columns = [ls[:, 0].mean(), ls[:, 1].mean(), ls[:, 2].mean()]
  
  var_rows = [ls[0, :].var(), ls[1, :].var(), ls[2, :].var()]
  var_columns = [ls[:, 0].var(), ls[:, 1].var(), ls[:, 2].var()]
  
  std_rows = [ls[0, :].std(), ls[1, :].std(), ls[2, :].std()]
  std_columns = [ls[:, 0].std(), ls[:, 1].std(), ls[:, 2].std()]
  
  max_rows = [ls[0, :].max(), ls[1, :].max(), ls[2, :].max()]
  max_columns = [ls[:, 0].max(), ls[:, 1].max(), ls[:, 2].max()]
  
  min_rows = [ls[0, :].min(), ls[1, :].min(), ls[2, :].min()]
  min_columns = [ls[:, 0].min(), ls[:, 1].min(), ls[:, 2].min()]
  
  sum_rows = [ls[0, :].sum(), ls[1, :].sum(), ls[2, :].sum()]
  sum_columns = [ls[:, 0].sum(), ls[:, 1].sum(), ls[:, 2].sum()]

  return {
    'mean': [mean_columns, mean_rows, ls.mean()],
    'variance': [var_columns, var_rows, ls.var()],
    'standard deviation': [std_columns, std_rows, ls.std()],
    'max': [max_columns, max_rows, ls.max()],
    'min': [min_columns, min_rows, ls.min()],
    'sum': [sum_columns, sum_rows, ls.sum()]
  }