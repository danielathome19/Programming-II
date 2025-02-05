# range(stop) -- stop is exclusive
# range(start, stop)
# range(start, stop, step)
for col1 in range(2, 11, 2):
    col2 = col1 + 1
    col3 = col1 * 2
    col4 = col1**2
    print(f"{col1}\t{col2}\t{col3}\t{col4}")
