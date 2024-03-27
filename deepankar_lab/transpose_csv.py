import pandas as pd


def transpose_csv(input_file, output_file):
    # Read input CSV file
    df = pd.read_csv(input_file)

    # Transpose DataFrame
    transposed_df = df.transpose()

    # Write transposed DataFrame to output CSV file
    transposed_df.to_csv(output_file)


# Example usage:
input_file = "output_file.csv"
output_file = "final.csv"
transpose_csv(input_file, output_file)
