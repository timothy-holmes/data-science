#%%
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_source = os.path.join(dir_path,'weather_data')
source_files = [os.path.join(dir_path_source, f) 
    for f in os.listdir(dir_path_source) 
    if os.path.isfile(os.path.join(dir_path_source, f))
    ]

print(source_files)
# %%
import pandas as pd
dfs = [pd.read_csv(f) for f in source_files]

# %%
# remove extra columns, rename cells
# wanted to avoid typing original column names... but I did
for df in dfs:
    df['date']=pd.to_datetime(df[['Year','Month','Day']])
    df = df.drop(df[pd.isna(df['Quality'])].index)
    for col in list(df.columns):
        if 'Maximum' in col:
            df_max = df[['date','Maximum temperature (Degree C)']].copy()
            df_max.rename(inplace=True,columns={'date':'date',col:'max temp'})
            df_max.set_index('date')
            continue
        if 'Minimum' in col:
            df_min = df[['date','Minimum temperature (Degree C)']].copy()
            df_min.rename(inplace=True,columns={'date':'date',col:'min temp'})
            df_min.set_index('date')
            continue

# merge min temp/max temp and remove values without either
dff = pd.merge(df_max, df_min,how='inner')
dff = dff.drop(dff[pd.isna(dff['max temp'])].index)
dff = dff.drop(dff[pd.isna(dff['min temp'])].index)

# %%

# create temp difference column
dff['diff'] = dff.apply(lambda row: row['max temp'] - row['min temp'], axis=1)

#%%

# group by months (not necessary)
"""
year_groups = dff.groupby(['year']) or .groupby(pd.Grouper(freq='Y'))

"""
#%%

# create rollling mean/std and take every 500th day
dff_ra = dff.rolling(window=4383,min_periods=1,center=True).mean().iloc[::500]
dff_std = dff.rolling(window=4383,min_periods=1,center=True).std().iloc[::500]

from matplotlib import pyplot as plt
# create plots, not going to bother prettifying
# rolling mean plot
fig,ax = plt.subplots()
ax.scatter(x=dff_ra.index,y=dff_ra['max temp'],color='blue')
ax.scatter(x=dff_ra.index,y=dff_ra['min temp'],color='green')
ax.scatter(x=dff_ra.index,y=dff_ra['diff'],color='red')
plt.show()

dir_path_plots = os.path.join(dir_path,'weather_plots')
if not os.path.exists(dir_path_plots):
    os.makedirs(dir_path_plots)
plt.savefig(os.path.join(dir_path_plots,'rolling_mean.jpg'))

# rolling std plot
fig,ax = plt.subplots()
ax.scatter(x=dff_std.index,y=dff_std['max temp'],color='blue')
ax.scatter(x=dff_std.index,y=dff_std['min temp'],color='green')
ax.scatter(x=dff_std.index,y=dff_std['diff'],color='red')
plt.show()
plt.savefig(os.path.join(dir_path_plots,'rolling_std.jpg'))