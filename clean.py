import pandas as pd
import argparse


def clean_data(input1, input2, output):
    # Read the input data files
    contact_df = pd.read_csv(input1)
    other_df = pd.read_csv(input2)

    # Merge the data based on ID
    merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')

    # Drop rows with missing values
    merged_df.dropna(inplace=True)


    # Drop rows with 'insurance' or 'Insurance' in the job column
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    merged_df=merged_df.drop(columns=["id"])
    print("Output shape:", merged_df.shape)

    # Save the cleaned data to the output file
    merged_df.to_csv(output, index=False)


if __name__ == '__main__':
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Data cleaning script')

    # Add the positional arguments
    parser.add_argument('input1', type=str, help='Path to respondent_contact.csv')
    parser.add_argument('input2', type=str, help='Path to respondent_other.csv')
    parser.add_argument('output', type=str, help='Path to the output file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the clean_data function
    clean_data(args.input1, args.input2, args.output)