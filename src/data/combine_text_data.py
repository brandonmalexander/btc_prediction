import pandas as pd


def combine_chunks(path1, path2):
    df1 = pd.read_csv(filepath_or_buffer=path1, infer_datetime_format=True)
    df1 = df1.set_index(df1.columns[0])
    df2 = pd.read_csv(filepath_or_buffer=path2, infer_datetime_format=True)
    df2 = df2.set_index(df2.columns[0])
    combined = df1.append(df2)
    return combined


chunk1 = 'reddit_raw_data.csv'
chunk2 = 'reddit_raw_data_4-22.csv'
bothChunks = 'raw_reddit_data_final.csv'


df = combine_chunks(chunk1, chunk2)

df.to_csv(path_or_buf=bothChunks)

# print(pd.read_csv(filepath_or_buffer=bothChunks, infer_datetime_format=True).head(5))
