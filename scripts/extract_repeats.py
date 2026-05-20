import pandas as pd
import gzip

species = snakemake.wildcards.species

rf = snakemake.input.rf
rc = snakemake.input.rc
sr = snakemake.input.sr

out = snakemake.output.tsv

# repeat_feature
rf_df = pd.read_csv(
    rf,
    sep="\t",
    header=None,
    compression="gzip"
)

rf_df = rf_df[[1,2,3,4,7]]

rf_df.columns = [
    "seq_region_id",
    "start",
    "end",
    "strand",
    "repeat_consensus_id"
]

# seq_region
sr_df = pd.read_csv(
    sr,
    sep="\t",
    header=None,
    compression="gzip"
)

sr_df = sr_df[[0,1]]

sr_df.columns = [
    "seq_region_id",
    "seq_region"
]

# repeat_consensus
rc_df = pd.read_csv(
    rc,
    sep="\t",
    header=None,
    compression="gzip"
)

rc_df = rc_df[[0,1,2,3]]

rc_df.columns = [
    "repeat_consensus_id",
    "repeat_name",
    "repeat_class",
    "repeat_type"
]

# merge
df = rf_df.merge(sr_df, on="seq_region_id")
df = df.merge(rc_df, on="repeat_consensus_id")

df["species"] = species
df["length"] = df["end"] - df["start"] + 1

cols = [
    "species",
    "seq_region",
    "start",
    "end",
    "strand",
    "repeat_name",
    "repeat_class",
    "repeat_type",
    "length"
]

df = df[cols]

df.to_csv(
    out,
    sep="\t",
    index=False,
    compression="gzip"
)
