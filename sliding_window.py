#!/usr/bin/env python3
import sys 
def sliding_window(k, kmer):
	slides = []
	len_kmer = len(kmer)
	for i in range(0, len(kmer)):
		print(i)
		stop = i + k
		print(stop)
		slide = kmer[i: stop]
		if len(slide) == 9:
			slides.append(slide)
	return(slides)
def gc_content(slides):
	gc_content = {}
	for s in slides:
		gc = 0
		s = s.lower()
		for n in s:
			if n == 'g' and n == 'c':
				gc +=1
		gc_con = gc/len(s)
		gc_content.update({s:gc_con})
	return(gc_content)
if __name__ == "__main__":
	k = int(sys.argv[1])
	
	kmer = str(sys.argv[2])
	r1 = sliding_window(k,kmer)
	print(r1)
	r2 = gc_content(r1)
	print(r2) 		
