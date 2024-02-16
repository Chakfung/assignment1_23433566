import pandas as pd

def clean(input1, input2):

    df_contact = pd.read_csv(input1)
    df_other = pd.read_csv(input2)

    merged_df = pd.merge(df_contact, df_other, left_on='respondent_id', right_on='id')
    merged_df = merged_df.drop(columns=['id']) 

    cleaned_df = merged_df.dropna()
    cleaned_df = cleaned_df[~cleaned_df['job'].str.contains('insurance|Insurance')]
    
    return cleaned_df

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file one (CSV)')
    parser.add_argument('input2', help='Data file two (CSV)')
    parser.add_argument('output', help='Merged and Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    print("the shape of the output file:", cleaned.shape)
    cleaned.to_csv(args.output, index=False)
    print("Data cleaning completed.")
