from pathlib import Path

inFp = None
inStr = ""

inFp = open(Path(__file__).with_name("data1.txt"), "r")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()
