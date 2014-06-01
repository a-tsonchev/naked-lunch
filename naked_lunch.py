import re
import random

with open('.naked_lunch.txt') as infile:

	terms = ['mugwump']

	no_lines = infile.read().replace('\n', ' ')
	no_elipses = no_lines.replace('...', ' ')
	sentences = no_elipses.split('.')
	pattern = re.compile(r'.*[^a-zA-Z]({0})[^a-zA-Z].*'.format('|'.join(terms)), re.IGNORECASE)
	goodthings = [line.strip() for line in sentences if pattern.match(line)]

print random.choice(goodthings) + '.'