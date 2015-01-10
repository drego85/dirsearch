import sys

fd = None
try:
    fd = open(sys.argv[1])
except IOError:
    sys.exit("Invalid file")

out = open(sys.argv[1] + ".d3", 'w')
for line in fd:
    if line.startswith("#"): continue
    out.write(line)
    out.write(line[:-1] + ".%EXT%\n")
out.flush()