#! /usr/bin/env python
' Build a command-line tool for counting word frequencies in natural text.'

# To make this executable on Linux/Mac systems:
# $ chmod +x frequency.py
# $ alias frequency='/Users/raymond/sj/frequency.py'
# $ ln -s /Users/raymond/sj/frequency.py /usr/local/bin/frequency

from collections import Counter
import re

__all__ = ['frequency']

def frequency(text, limit=50, word_pattern=r"[a-z]+(?:['-][a-z]+)?"):
    'Analyze text return a truncated list of (word, count) pairs in order of decreasing frequency'
    words = re.findall(word_pattern, text.lower())
    return Counter(words).most_common(limit)

if __name__ == '__main__':
    import sys
    from pprint import pprint

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print >> sys.stderr, "Usage:  frequency filename [limit=10]"
        sys.exit(1)
    filename = sys.argv[1]
    limit = 10
    if len(sys.argv) == 3:
        limit = int(sys.argv[2])
    
    with open(filename) as f:
        text = f.read()

    pprint(frequency(text, limit=limit))
