#merge two csvs
import pandas as pd

def get_base_column_name(column_name):
    if '_heavy' in column_name:
        return column_name.replace('_heavy', '')
    elif '_light' in column_name:
        return column_name.replace('_light', '')
    return column_name

df1 = pd.read_csv('/home/mahek0423/sheep/sheepH_file.csv')  # Replace with your first CSV file path
df2 = pd.read_csv('/home/mahek0423/sheep/sheepL_file.csv')  # Replace with your second CSV file path

df1_base_columns = set([get_base_column_name(col) for col in df1.columns if '_heavy' in col])
df2_base_columns = set([get_base_column_name(col) for col in df2.columns if '_light' in col])

common_base_columns = df1_base_columns.intersection(df2_base_columns)


df1_columns_to_merge = [col for col in df1.columns if get_base_column_name(col) in common_base_columns]
df2_columns_to_merge = [col for col in df2.columns if get_base_column_name(col) in common_base_columns]

df1_common = df1[df1_columns_to_merge]
df2_common = df2[df2_columns_to_merge]

df1_common.columns = [col.replace('_heavy', '') + '_heavy' for col in df1_common.columns]
df2_common.columns = [col.replace('_light', '') + '_light' for col in df2_common.columns]

merged_df = pd.concat([df1_common, df2_common], axis=1)

merged_df.to_csv('/home/mahek0423/sheep/MERGED_file.csv', index=False)

print(merged_df)
