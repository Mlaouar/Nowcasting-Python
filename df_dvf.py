# -------------------------------------------------Libraries
import os
from datetime import datetime as dt
from Functions.load_spec import load_spec
from Functions.load_data import load_data
from Functions.dfm import dfm
import pickle
from Functions.summarize import summarize
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# -------------------------------------------------Set dataframe to full view
pd.set_option('display.expand_frame_repr', False)


sample_start = dt.strptime("2014-01-01", '%Y-%m-%d').date().toordinal() + 366  # estimation sample

# Load model specification structure `Spec`
Spec = load_spec('spec_dvf.xls')


# Load data
X, Time, Z = load_data("data_dvf.xlsx", Spec, sample_start)


# -------------------------------------------------Run dynamic factor model (DFM) and save estimation output as 'ResDFM'.
threshold = 1e-4  # Set to 1e-5 for more robust estimates
Res = dfm(X, Spec, threshold)
Res = {"Res": Res, "Spec": Spec}

