# plancTE Repeat Extractor

Pipeline em Snakemake para extração e sumarização de elementos repetitivos do Ensembl Plants.

## Features

- Extração automática de repeats
- Processamento paralelo
- Suporte a centenas de genomas
- Outputs TSV/BED
- QC por espécie
- Relatórios comparativos

## Estrutura esperada

data/mysql/<species>/

com:

- repeat_feature.txt.gz
- repeat_consensus.txt.gz
- seq_region.txt.gz

## Instalação

```bash
conda env create -f envs/environment.yaml
conda activate <env>


## Output columns

| Column | Description |
|---|---|
| species | Species name |
| seq_region | Chromosome/scaffold |
| start | Repeat start |
| end | Repeat end |
| strand | Strand |
| repeat_name | Repeat family |
| repeat_class | Repeat class |
| repeat_type | Repeat type |
| length | Repeat length |
