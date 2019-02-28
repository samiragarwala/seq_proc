# To run file: python2.7 run.py /Users/Samir/desktop/ParkerLab/HG00247.cram seq.bam out.bw

from proc import Sequence_Processing

processing = Sequence_Processing()

processing.cram2bam()
# processing.bam2bigWig()

# Convert BAM to BedGraph using bedtools: genomeCoverageBed -ibam seq.bam -bg -trackline -split -g ... > out.bedGraph
# Convert BedGraph to BigWig: bedGraphToBigWig out.bedGraph chrom.sizes out.bw