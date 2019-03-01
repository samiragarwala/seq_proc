# To run file: python run.py <CRAM File Directory> <BW File Directory> <Path to bedGraphToBigWig> <Path to Chromosome sizes file>

from proc import Sequence_Processing
import sys
import os
import glob

#directory to cram files 
cram = sys.argv[1]

#directory to save big wig files
bw = sys.argv[2]

# path to unix executable bedGraphToBigWig
exe = sys.argv[3]

# path to chromosome sizes file
sizes = sys.argv[4]

processing = Sequence_Processing(exe,sizes)

count = 0;

for filename in glob.glob(os.path.join(cram, '*.cram')):
	
	# counting number of files
	count = count + 1
	print('\033[1m' + 'File ' + str(count) + '\033[0m')

	head, tail = os.path.split(filename)
	name,extension = os.path.splitext(tail)

	processing.cram2bam(filename, bw + '/' + name )

	processing.bam2bigWig(bw + '/' + name)

# Convert BAM to BedGraph using bedtools: genomeCoverageBed -ibam seq.bam -bg -trackline -split -g ... > out.bedGraph
# Convert BedGraph to BigWig: bedGraphToBigWig out.bedGraph chrom.sizes out.bw
	#In chrom.sizes file of assembly Hg19: remove chr before chr1,chrX, etc. Also change chromMt to MT.
	# Note: Displaying particular line in data file: sed -n 'eline_num,40p' file_name
	# Note: Delete particular line in data file using eg. for line 3: sed -i '3d' filename. In our case last line was being problematic and thus deleted.
