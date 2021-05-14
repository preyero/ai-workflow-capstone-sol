#!/usr/bin/env python
"""
collection of helper functions
"""

import time, os, re, shutil
import pandas as pd


def comp_time(run_start):
    """ Compute time since a Time.time() object """
    m, s = divmod(time.time()-run_start,60)
    h, m = divmod(m, 60)
    print("load time:", "%d:%02d:%02d"%(h, m, s))


def check_col_names(d_path, verbose=False):
    "Check consistency of column names of json files in data path"
    # get file list
    file_list = [os.path.join(d_path, f) for f in os.listdir(d_path)
                 if re.search("\.json", f)]

    # fetch source json files
    col_names = {}
    for f_name in file_list:
        invoice = f_name.split("/")[-1]  # also os.path.split()
        if verbose:
            print("Importing {}:".format(invoice))
        df_i = pd.read_json(f_name)
        col_names[invoice] = list(df_i.columns)

    col_names = pd.DataFrame(data=col_names.values(),
                             index=col_names.keys())
    return col_names


def load_csv_to_ts(filename):
    ts = pd.read_csv(filename, index_col=0, parse_dates=True)
    return ts


def import_csv_to_ts(data_dir, clean=False):
    """
    Load csv files from ts-data as a time-series DataFrame
    uses csv to load quickly
    use clean=True when you want to re-create the files
    """
    ts_data_dir = os.path.join(data_dir, "ts-data")

    if clean:
        if os.path.exists(ts_data_dir):
            shutil.rmtree(ts_data_dir)
    if not os.path.exists(ts_data_dir):
        os.mkdir(ts_data_dir)

    ## if files have already been processed load them
    if len(os.listdir(ts_data_dir)) > 0:
        print("... loading ts data from files")
        # Load as time-series DataFrame:
        return ({re.sub("\.csv", "", cf)[3:]: load_csv_to_ts(os.path.join(ts_data_dir, cf))
                 for cf in os.listdir(ts_data_dir)})

    else:
        raise Exception("Time series csv files cannot be found. Run fetch_ts first")


def convert_df_to_ts(df, col):
    df['datetime'] = pd.to_datetime(df[col])
    df = df.set_index('datetime')
    df.drop(['date'], axis=1, inplace=True)
    df.head()
    return df




