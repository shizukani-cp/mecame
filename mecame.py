import argparse
from janome.tokenizer import Tokenizer

parser = argparse.ArgumentParser(description="This is mecab(?).")
parser.add_argument("fromf")
parser.add_argument("savef")
args = parser.parse_args()
FROMF = args.fromf
SAVEF = args.savef
tokenizer = Tokenizer()

text = ""
with open(FROMF, "r", encoding="utf-8") as f:
    for row in f:
        for t in tokenizer.tokenize(row, wakati=True):
            text += f"{str(t)} "

with open(SAVEF, "w", encoding="utf-8") as f:
    f.write(text)