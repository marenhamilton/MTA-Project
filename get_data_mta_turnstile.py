#%%
from datetime import datetime, timedelta
import pandas as pd
import pickle
#%%
def get_data_from_mta(file_url):
    data = pd.read_csv(file_url)
    return data

def get_data_from_date_list(dates):
    df_list = []
    for x in dates:
        string = ('http://web.mta.info/developers/data/nyct/turnstile/turnstile_' + x + '.txt')
        holder_df = get_data_from_mta(string)
        df_list.append(holder_df)
    return pd.concat(df_list)
    
def next_sat(startdate,enddate) :
   """
   startdate/enddate : 'MM-DD-YYYY'
   returns list of dates as YYMMDD strings between the dates, not including the enddate
   """
   dates = []
   begin = datetime.strptime(startdate,'%m-%d-%Y')
   end = datetime.strptime(enddate,'%m-%d-%Y')
   current = begin
   while current < end :
       dates.append(current.strftime('%y%m%d'))
       current += timedelta(days=7)
   return dates

def march_thru_jun(dates) :
   return [date for date in dates if int(date[3]) in range(3,7)]


#%%
dates = march_thru_jun(next_sat('01-02-2016', '01-01-2019'))
#%%
mta_turnstile_data = get_data_from_date_list(dates)
#%%
with open('mta_data.pickle', 'wb') as to_write:
    pickle.dump(mta_turnstile_data, to_write)

