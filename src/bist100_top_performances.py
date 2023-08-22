import numpy as np
import pandas as pd

df_perf = pd.read_html("../data/bist100/bist100_performans_20230723.csv", encoding="utf-8")[0]
df_temel = pd.read_html("../data/bist100/bist100_temel_20230723.csv", encoding="utf-8")[0]
df_perf.drop(["Unnamed: 0"], axis=1, inplace=True)
df_temel.drop(["Unnamed: 0"], axis=1, inplace=True)

def remove_abbr(x):
    if "K" in x:
        x = float(x.replace("K", ""))*1000
    elif "M" in x:
        x = float(x.replace("M", ""))*1000000
    elif "B" in x:
        x = float(x.replace("B", ""))*1000000000
    return x

def quantify_temel_columns(df):
    for col in df.columns.drop("İsim"):
        print(col)
        df[col] = df[col].fillna("0").str.replace(",", ".")
        df[col] = df[col].fillna("0").apply(remove_abbr)
        df[col] = df[col].astype("float64")
    return df


def quantify_perf_columns(df):
    for col in df.columns.drop("İsim"):
        df[col] = df[col].fillna("0").str.replace(".", "").str.replace(",", ".").str.replace("%", "").replace("-","0").astype("float64")

    return df

df_temel = quantify_temel_columns(df_temel)
df_perf = quantify_perf_columns(df_perf)

df_temel = df_temel.sort_values("F/G Oranı", ascending=False)
df_perf_month_1 = df_perf.sort_values("1 Aylık", ascending=False)
df_perf_ytd = df_perf.sort_values("YTD", ascending=False)

#df_final = df_perf_ytd.head(42).merge(df_perf_month_1.head(42), on="İsim").merge(df_temel.head(42), on = "İsim")
df_final = df_perf_month_1.head(42).merge(df_temel.head(42), on = "İsim")
#df_final = df_final[["İsim", "Günlük_x", "1 Aylık_x", "YTD_x"] + df_temel.drop(["İsim"], axis=1).columns.to_list()]
print(df_final)
print(df_final.shape)