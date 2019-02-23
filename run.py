# To run file: python2.7 run.py /Users/Samir/desktop/ParkerLab/HG00247.cram seq.bam out.bw

from proc import Sequence_Processing

processing = Sequence_Processing()

processing.cram2bam()
processing.bam2bigWig()