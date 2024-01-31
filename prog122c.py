# range(stop)               [0, 9)
# range(start, stop)        [start, stop)
# range(start, stop, step)  [start, stop)
for lcv in range(2, 11, 2):
  col2 = lcv + 1
  col3 = lcv * 2
  col4 = lcv**2
  print(f"{lcv}\t{col2}\t{col3}\t{col4}")
