#Project Outline - Analysis of transcriptome sequencing  data acquired from cortical samples in living Parkinson's disease patients
##Background
The trancriptomic profile of the central nervous system (CNS) of living Parkinson’s disease (PD) patients is as yet undefined and may offer critical biomarkers to define pathogenic mechanisms, new therapeutic targets, early diagnosis and disease progression. To this end, we have been examining the transcriptome by sequencing RNA isolated from brain specimens in living PD and control patients to look for gene expression alterations and relevant mutations. So far, total RNA was extracted from cortical biopsies in 6 patients with PD and 6 healthy controls and sequenced on the Illumina HiSeq 2500 platform using Illumina TruSeq chemistries. Paired-end reads, approximately 90 million per sample, were trimmed to remove adapters and low quality bases; aligned to the human genome (Hg19); raw counts generated using HTSeq (v.0.6.1p2); and analyzed for differential expression using edgeR (v.3.8.6). The variant calling tools annovar and GATK were also used to identify variants. 

##Data
The data I am working with consists of several types of files including trimmed fastq files, aligned bam files and tsv files with differential expression/SNP data

###Fastq/BAM files
- Fastq files are very large and gzipped. Unknown number of observations. Should contain fragment sequences as well as quality scores for each.
- BAM files are also large and binary. Would need to be converted to SAM format to work with them directly.

###Differential expression tsv file
####Observations
25374 raw observations, filtered to 18003 by removing genes with less than 10 reads per sample
####Variables
19 variables:
1. Gene Name: name of identified gene
2. EGID: Entrez Gene ID, a numeric identifier for the gene
3. logFC: log base 2 fold change of the particular gene, comparing PD samples to controls
4. logRPKM: moderated log base 2 reads per kilobase per million for the gene overall
5. LR: Likelihood ratio test values showing goodness of fit
6. PValue: measure of statistical significance of the differential expression
7. FDR: False discovery rate, a measure of statistical significance corrected for multiple comparisons
8. Individual RPKM values (12): Counts for each individual sample

###Variant calling tsv file
####Observations
12 tsv files containing variant data for each separate sample. Approximately 67k obersvations for every sample.
####Variables
131 variables:
CHROM	POS	ID	REF	ALT	QUAL	FILTER	AC	AF	AN	BaseQRankSum	ClippingRankSum	DP	DS	FS	HaplotypeScore	InbreedingCoeff	MLEAC	MLEAF	MQ	MQ0	MQRankSum	QD	ReadPosRankSum	OVCF_KEY	MULTI_ALLELIC	M_ORDER	RNA_1:GTR	RNA_1:AD_REF	RNA_1:AD_ALT	RNA_1:DP	RNA_1:GQ	RNA_1:GT	RNA_1:PL	RNA_1:OGT	RNA_1:OZYG	RNA_1:Zygosity	typeseq	typeseq_priority	refseq_id	aa_flag	effect	effect_priority	leftD	rightD	gene_symbol	entrez_id	gene_desc	gene_type	omim_id	omim_phenotype	MPO	HPO	CGD_disease	CGD_inheritance	ExAc_mis_z	ExAc_lof_z	ExAc_pLI	Clinvar_mis_pathogenic_count	Clinvar_mis_benign_count	Clinvar_lof_pathogenic_count	Clinvar_lof_benign_count	Clinvar_SIG	Clinvar_CLNREF	Clinvar_CLNACC	HGMD_Accession	HGMD_type	HGMD_tag	HGMD_Disease	HGMD_PubmedId	cosmic	1000g_all	1000g_eur	1000g_amr	1000g_eas	1000g_afr	1000g_sas	NHLBI_all	NHLBI_aa	NHLBI_eu	ExAC_Freq	ExAC_AFR	ExAC_AMR	ExAC_EAS	ExAC_FIN	ExAC_NFE	ExAC_OTH	ExAC_SAS	cg	cg_filtered	cgW597_AllFreq	cgW597_CalledFreq	cgW597_11s	cgW597_Hs	cgW597_Ls	cg1KG436_AllFreq	cg1KG436_CalledFreq	cg1KG436_11s	cg1KG436_Hs	cg1KG436_Ls	dbsnp	dbsnp_common	dbsnp_region	dbsnp_common_region	dbsnp_wind	sift_score	PROVEAN_score	polyphen_score	ma_score	mt_score	CADD_Raw	CADD_phred	phylopPMam	phylopPMam_avg	phylopVert100	phylopVert100_avg	phastCons_placental	pfam_annovar	per_cds_affected	per_transcripts_affected	spx_gene	spx_transcript	spx_exon_number	spx_ss_dist	spx_wt_psi	spx_sequence_event_type	spx_dpsi	dbscSNV_ADA_SCORE	dbscSNV_RF_SCORE	SegDup	Repeat

Too many variables to describe individually and I'm still not familiar with what many of these signify. I'm particularly interested in the filter row which shows what type of variant is detected. 

##Objectives
###Differential Expression
 - Subset the data based on fold change and FDR thresholds with various cutoffs (eg. FDR <.05 & logFC > .58, 1, 2)
 - Generate data visualisations in python to examine the data using packages such as Matplotlib or Seaborn

###Variants
- Qualitative and quantitative examination of values of the Filter variable (eg. SNPCluster counts)
- Ideally it would be interesting to find a way to automate pulling out variants at the location of the top differentially expressed genes 