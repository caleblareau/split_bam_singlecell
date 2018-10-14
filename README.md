# Split bam based on sam tag attribute

*Contact* [Caleb Lareau](mailto:clareau@broadinstitute.org)

Python functionality for splitting bam based on sam tag and dictionary file

Suppose that we have some single cell data that has been clustered, and we
want to split the bam files based on the cluster id. Encode this information
in a two column tsv format:
```
head cluster_dictionary_small.tsv 
N702_Exp119_sample2_S1_BC0005_N01	14
N702_Exp119_sample2_S1_BC0008_N02	1
N702_Exp119_sample2_S1_BC0010_N01	2
N702_Exp119_sample2_S1_BC0011_N02	10
N702_Exp119_sample2_S1_BC0014_N01	2
N702_Exp119_sample2_S1_BC0015_N01	2
N702_Exp119_sample2_S1_BC0016_N01	9
N702_Exp119_sample2_S1_BC0017_N01	15
N702_Exp119_sample2_S1_BC0018_N02	14
N702_Exp119_sample2_S1_BC0019_N01	19
```

where the left is the cell ID and the right is the cluster / attribute ID

Then, given a `.bam` file with an attribute (e.g. the `XB` tag) that matches the left (cell ID) column:

```
samtools view small.bam | head
NS500711:171:HC5F7BGX9:4:12507:13214:18646	147	chr10	3261372	43	2S38M	=	3261338	-72	ATCAGCTTCCATCTTCCCCTTCCTTTTACTTCTCTGCCAC	E//EEEE//AE//E6EE/6EEEE//AE/A/A/AEAA6AA6	NM:i:3	MD:Z:9G15C1C10	AS:i:23	XS:i:21XA:Z:chr17,-18793947,6S21M13S,0;chr12,+81126677,19S21M,1;chr8,-90857290,16S19M5S,0;	XB:Z:gtccttcttaagcgaacgtaa	NS:i:1	DB:Z:N702_Exp119_sample2_S1_BC3875_N02	RG:Z:N702_Exp119_sample2-49AFDDFB-708A0293
NS500711:171:HC5F7BGX9:2:21312:17028:14716	83	chr10	3274475	60	40M	=	3274196	-319	AGGAGACACGGCAGCACATAGGCAGACATGGTCCTAGAGA	/<<EEA//EEAEE6/AEEEEA<///E<//E/E<E/<EAEE	NM:i:0	MD:Z:40	AS:i:40	XS:i:26	XB:Z:tagtaccacgtattacgtatt	NS:i:2	DB:Z:N702_Exp119_sample2_S1_BC3567_N03	RG:Z:N702_Exp119_sample2-63BAD4F0-2FDA7C0A
NS500711:171:HC5F7BGX9:1:11210:15303:17781	163	chr10	3365677	60	40M	=	3365963	326	CGTTATAATAAGCTCATTCATTCGTAATTCTTCTTGGTTG	AAAAAEAEEE6EEEEEEEEEEEEEEEEEEEEEEEEEEEEE	NM:i:0	MD:Z:40	AS:i:40	XS:i:0	XB:Z:acgtattggagcctactcaat	NS:i:2	DB:Z:N702_Exp119_sample2_S1_BC2175_N03	RG:Z:N702_Exp119_sample2-73468AD7
NS500711:171:HC5F7BGX9:2:11204:5257:1424	163	chr10	3365769	60	40M	=	3365968	239	GGCAAGGAGGGAGAGGTTGCTTAGAAAGGGCCCTGGGAGG	6A/AAEEE6/EEEEEE6EAEEEE6E66/AEEAEEA/AEAE	NM:i:0	MD:Z:40	AS:i:40	XS:i:19	XB:Z:tagtgttcgcaatcctattcg	NS:i:6	DB:Z:N702_Exp119_sample2_S1_BC0080_N02	RG:Z:N702_Exp119_sample2-63BAD4F0-2FDA7C0A
NS500711:171:HC5F7BGX9:1:11210:15303:17781	83	chr10	3365963	60	40M	=	3365677	-326	AAAACCAGTCTGCGAATAATTCCTGAGGCACGGTGACTGC	EEEEEAE/AEEA/AEEEEEEEEEE<EE/EE<EE<EEEE<E	NM:i:1	MD:Z:12G27	AS:i:35	XS:i:0	XB:Z:acgtattggagcctactcaat	NS:i:2	DB:Z:N702_Exp119_sample2_S1_BC2175_N03	RG:Z:N702_Exp119_sample2-73468AD7
```

we want to create a bunch of different bam files for each value in the second file of the dictionary. 

This can be done with this script

```
python code/bam_attr_split.py -i test/small.bam -d test/cluster_dictionary_small.tsv -t DB
```

this will then create the following:

```
-rw-r--r--  1 lareauc  staff    26K Oct 13 23:27 small.24.bam
-rw-r--r--  1 lareauc  staff   262K Oct 13 23:27 small.25.bam
-rw-r--r--  1 lareauc  staff   742K Oct 13 23:27 small.20.bam
-rw-r--r--  1 lareauc  staff    47K Oct 13 23:27 small.21.bam
-rw-r--r--  1 lareauc  staff   239K Oct 13 23:27 small.22.bam
-rw-r--r--  1 lareauc  staff    84K Oct 13 23:27 small.23.bam
-rw-r--r--  1 lareauc  staff   164K Oct 13 23:27 small.1.bam
-rw-r--r--  1 lareauc  staff   310K Oct 13 23:27 small.3.bam
-rw-r--r--  1 lareauc  staff   1.0M Oct 13 23:27 small.2.bam
-rw-r--r--  1 lareauc  staff    32K Oct 13 23:27 small.5.bam
-rw-r--r--  1 lareauc  staff    61K Oct 13 23:27 small.4.bam
-rw-r--r--  1 lareauc  staff   118K Oct 13 23:27 small.7.bam
-rw-r--r--  1 lareauc  staff   279K Oct 13 23:27 small.6.bam
-rw-r--r--  1 lareauc  staff   1.0M Oct 13 23:27 small.9.bam
-rw-r--r--  1 lareauc  staff   458K Oct 13 23:27 small.8.bam
-rw-r--r--  1 lareauc  staff   326K Oct 13 23:27 small.11.bam
-rw-r--r--  1 lareauc  staff   406K Oct 13 23:27 small.10.bam
-rw-r--r--  1 lareauc  staff    72K Oct 13 23:27 small.13.bam
-rw-r--r--  1 lareauc  staff   572K Oct 13 23:27 small.12.bam
-rw-r--r--  1 lareauc  staff   268K Oct 13 23:27 small.15.bam
-rw-r--r--  1 lareauc  staff   381K Oct 13 23:27 small.14.bam
-rw-r--r--  1 lareauc  staff   109K Oct 13 23:27 small.17.bam
-rw-r--r--  1 lareauc  staff    56K Oct 13 23:27 small.16.bam
-rw-r--r--  1 lareauc  staff   1.4M Oct 13 23:27 small.19.bam
-rw-r--r--  1 lareauc  staff    54K Oct 13 23:27 small.18.bam
```

These will be sorted, so you can immediately index them

```
for i in *bam; do samtools index $i; done
```

