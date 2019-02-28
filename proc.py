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
		outfile = pysam.AlignmentFile(self.bam_name, "wb", header = samfile.header)
		# outfile = pysam.AlignmentFile(self.bam_name, "wb", header = samfile.header, template=samfile)

		#writing each read to bam file
		for read in samfile:
			outfile.write(read)

		outfile.close()
		samfile.close()

		pysam.index(self.bam_name)

		print('BAM File Created')

	# def bam2bigWig(self):

	# 	#function for converting bam to bigWig

	# 	#install pyGenomeTracks library before use
	# 	os.system('bamCoverage -b ' + self.bam_name + ' -o ' + self.bw_name)

	# 	print('BigWig File Created')
