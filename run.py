# To run file: python3 run.py /Users/Samir/desktop/ParkerLab/HG00247.cram seq.bam seq.bw /Users/Samir/desktop/ParkerLab/Libaries/bcbb/nextgen/scripts/

from proc import Sequence_Processing

processing = Sequence_Processing()

processing.cram2bam()
processing.bam2bigWig()