import sys
import os
import numpy as np
import pysam

class Sequence_Processing:

	def __init__(self, path1, path2):

		# Storing filenames for input file, BAM file & BigWig file

		self.u_path = path1

		self.chrom = path2


	def cram2bam(self, cram_path, bam_path):

		#reading cram file
		print('Reading CRAM File')
		samfile = pysam.AlignmentFile(cram_path, "rc")

		#creating output bam file
		outfile = pysam.AlignmentFile(bam_path + '.bam', "wb", header = samfile.header)
		# outfile = pysam.AlignmentFile(self.bam_name, "wb", header = samfile.header, template=samfile)

		#writing each read to bam file
		for read in samfile:
			outfile.write(read)

		outfile.close()
		samfile.close()

		pysam.index(bam_path + '.bam')

		print('BAM File Created')

	def bam2bigWig(self,bw_path):

		#function for converting bam to bigWig
		os.system('genomeCoverageBed -ibam ' + bw_path + '.bam' + ' -bg -trackline -split -g ... > ' + bw_path + '.bedGraph')
		print('Created BedGraph File')

		# sorting bedGraph file
		os.system('sort -k1,1 -k2,2n ' + bw_path + '.bedGraph' + ' > ' + bw_path + '_sorted.bedGraph') 
		print('Sorted BedGraph File')

		#deleting empty last line of BedGraph file which comes after sorting
		os.system("sed -ie '$d' " + bw_path + '_sorted.bedGraph')
		print('Processed BedGraph File')

		os.system(self.u_path + ' ' + bw_path +  '_sorted.bedGraph ' + self.chrom + ' ' + bw_path + '.bw')
		print('Created BigWig File')

		os.system('sudo rm ' + bw_path + '.bedGraph')
		os.system('sudo rm ' + bw_path + '_sorted.bedGraph')
		os.system('sudo rm ' + bw_path + '_sorted.bedGraphe')
		os.system('sudo rm ' + bw_path + '.bam')
		os.system('sudo rm ' + bw_path + '.bam.bai')
		print('Deleted BedGraph and BAM data files \n')





