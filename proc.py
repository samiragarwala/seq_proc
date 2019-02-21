import sys
import os
import numpy as np
import pysam


class Sequence_Processing:

	def __init__(self):

		# Storing filenames for input file, BAM file & BigWig file
		self.filename = sys.argv[1]

		self.bam_name = sys.argv[2]

		self.bw_name = sys.argv[3]


	def cram2bam(self):

		#reading cram file
		samfile = pysam.AlignmentFile(self.filename, "rc")

		#creating output bam file
		outfile = pysam.AlignmentFile(self.bam_name, "wb", template = samfile)

		#writing each read to bam file
		for read in samfile:
			outfile.write(read)

		outfile.close()
		samfile.close()

	def bam2bigWig(self):

		# adding local path to cloned GitHub repo (https://github.com/chapmanb/bcbb)
		#local path: '/Users/Samir/desktop/ParkerLab/Libaries/bcbb/nextgen/scripts/'
		sys.path.insert(0, sys.argv[4])

		#running script for converting bam to bigWig
		os.system('python3 bam_to_wiggle.py ' + self.bam_name + ' --outfile='+ self.bw_name)
