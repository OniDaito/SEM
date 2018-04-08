"""
Convert our hex dump files to binary dumps

"""


import sys, os, argparse

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Convert hex to bin dumps.')
  parser.add_argument('path', help='path to hex file')
  args = parser.parse_args()

  if args.path:
    out_path = os.path.splitext(args.path)[0] + ".bin"

    with open(args.path, 'r') as f:
      with open(out_path, 'wb') as g:
        for line in f.readlines():
          line = line.replace(" ","")
          line = line.replace("\n","")
          bb = bytes.fromhex(line)
          g.write(bb)