# To run file: python2.7 run.py /Users/Samir/desktop/ParkerLab/HG00247.cram seq.bam out.bw

from proc import Sequence_Processing

processing = Sequence_Processing()

processing.cram2bam()
# processing.bam2bigWig()

# Convert BAM to BedGraph using bedtools: genomeCoverageBed -ibam seq.bam -bg -trackline -split -g ... > out.bedGraph
# Convert BedGraph to BigWig: bedGraphToBigWig out.bedGraph chrom.sizes out.bw
	#In chrom.sizes file of assembly Hg19: remove chr before chr1,chrX, etc. Also change chromMt to MT.
	# Note: Displaying particular line in data file: sed -n 'eline_num,40p' file_name
	# Note: Delete particular line in data file using eg. for line 3: sed -i '3d' filename. In our case last line was being problematic and thus deleted.
