https://my.newtonschool.co/playground/code/heqlj85for0f


def bubbleSort(seq):
    
  # loop to access each array element
  for i in range(len(seq)):

    for j in range(0, len(seq) - i - 1):

      if seq[j] > seq[j + 1]:

        temp = seq[j]
        seq[j] = seq[j+1]
        seq[j+1] = temp
  return seq
