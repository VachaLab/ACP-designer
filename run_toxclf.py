import argparse
from pathlib import Path
import pandas as pd

from src.config import OUTPUT_PATH, CTT_PATH, DEVICE
from src.filters.f_cytotox import CytotoxicityFilter

def main(args):
    
    input_csv = args.input
    output_csv = args.output
    device = args.device

    # load input DF
    df = pd.read_csv(input_csv,index_col=False)

    # run classification
    clf = CytotoxicityFilter(CTT_PATH, device)
    results_df = clf.filter_sequences(df)

    print(f'\n\n saving results to: {str(output_csv)}')
    results_df.to_csv(output_csv,index=False)

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input',
        type=Path,
        help="path to input CSV file"
    )

    parser.add_argument(
        '--output',
        type=Path,
        default= OUTPUT_PATH / 'predictions.csv',
        help="path to output CSV file"
    )

    parser.add_argument(
        '--device',
        type=str,
        choices=['cpu', 'cuda', 'mps'],
        default=DEVICE,
        help="device for computation"
    )

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    
    args = parse_args()
    main(args)