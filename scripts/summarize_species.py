import pandas as pd

infile = snakemake.input[0]
outfile = snakemake.output[0]

df = pd.read_csv(infile, sep="\t")

summary = {
    "species": [df["species"].iloc[0]],
    "total_repeats": [len(df)],
    "total_repeat_bp": [df["length"].sum()],
    "n_repeat_classes": [df["repeat_class"].nunique()],
    "top_repeat_class": [
        df["repeat_class"].value_counts().idxmax()
    ]
}

summary_df = pd.DataFrame(summary)

summary_df.to_csv(outfile, sep="\t", index=False)
