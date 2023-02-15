import sys  # Provides access to command line args


def main(args):
  # C-style "Main/Entrypoint" Function
  if len(args) <= 0:
    print("Hello!")
    return
  print("Hello,", args[0])
  for arg in args:
    print(arg)


if __name__ == "__main__":
  main(sys.argv[1:])
