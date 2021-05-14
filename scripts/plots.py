#!/usr/bin/env python
"""
collection of functions for plotting
"""
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

IMG_DIR = os.path.join(".","images")
if not os.path.exists(IMG_DIR):
    os.mkdir(IMG_DIR)

plt.style.use('seaborn')

SMALL_SIZE = 12
MEDIUM_SIZE = 14
LARGE_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=LARGE_SIZE)   # fontsize of the figure title

def plot_horizontal_bar_chart(df, x_val, y_val, filename=None):
    fig = plt.figure(figsize=(20, 16))
    ax2 = fig.add_subplot(111)

    table2 = pd.pivot_table(df, index=[x_val], values=y_val)
    table2.plot(kind='barh', ax=ax2)
    ax2.set_xlabel(y_val)
    if filename is not None:
        fig.savefig(filename)


def plot_multiple_bar_graph(df, x_val, y_val, by_val, filename=None):
    fig = plt.figure(figsize=(12, 10))
    ax1 = fig.add_subplot(111)

    table1 = pd.pivot_table(df, index=x_val, columns=by_val, values=y_val)
    table1.plot(kind='bar', ax=ax1)
    ax1.set_ylabel(y_val)

    if filename is not None:
        fig.savefig(filename)


def plot_ts(ts, cols_plot, title=None, filename=None, join=True):
    fig = plt.figure(figsize=(16, 12))
    plt.tight_layout()
    ax1 = fig.add_subplot(111)

    if join:
        ts[cols_plot].plot(ax=ax1, subplots=True, alpha=0.5)
    else:
        ts[cols_plot].plot(ax=ax1, alpha=0.5)

    if title is not None:
        plt.suptitle(title)
    if filename is not None:
        fig.savefig(filename)



