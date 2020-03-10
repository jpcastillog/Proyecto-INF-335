import twint
import os
import glob 
import pandas as pd

hashtags = ['#chile', '#Chile', '#ChileViolaLosDerechosHumanos', '#ChileViolatesHumanRights', '#Noestamosenguerra', '#Piñerarenuncia', '#lamarchamásgrandedeChile','#ChileDesperto', '#Chiledesperto']
custom_retrieve = ['date', 'timezone', 'user_id', 'username', 'tweet', 'hashtags', 'geo', 'source']


def get_twitts(hashtags, file_name, since_date, until_date, format = '', limit = 100, custom = []):    
    words_to_find = hashtags[0]
    hashtags.pop(0)
    for h in hashtags:
        words_to_find += f' OR {h}'
    print(words_to_find)
    c = twint.Config()
    if format:
        c.Format = format
    if len(custom):
        c.Custom['tweet']= custom
    c.Search = words_to_find 
    c.Store_csv = True
    c.Since = since_date
    c.Until = until_date
    c.Limit = limit
    c.Output = file_name
    c.Lang = "es"
    c.Hide_output = True
    twint.run.Search(c)
    

def merge_files(remove = False):
    os.chdir('./temp_files')
    print(os.getcwd())
    extension = 'csv'
    all_filenames = [i for i in glob.glob(f'*.{extension}')]
    print(all_filenames)
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.to_csv('all_data.csv', index=False, encoding='utf-8')

    # Remove file of dir
    if remove:
        for file in all_filenames:
            os.remove(file)

# dates: lista de fechas sin hora
def get(hashtags, limit=1000):
    dates = ["2019-10-18", '2019-10-19', '2019-10-20', '2019-10-25', '2019-11-11']
    for d in dates:
        split = d.split('-')
        print(split)
        since_day = int(split[-1])
        until_day = since_day +  1
        print(since_day)
        print(until_day)
        since_day = str(since_day) if len(str(since_day)) > 1 else f'0{since_day}'
        until_day = str(until_day) if len(str(until_day)) > 1 else f'0{until_day}'
        print(since_day)
        print(until_day)
        since_date = f'{split[0]}-{split[1]}-{since_day}'
        until_date = f'{split[0]}-{split[1]}-{until_day}'
        
        file_name = f'./temp_files/{d}.csv'
        get_twitts(hashtags=hashtags, file_name=file_name, since_date=since_date, until_date=until_date, custom=[],limit=limit)

get(hashtags, limit=10000)
# merge_files()
# get_twitts(hashtags, 'test_data.csv', since_date = "2019-10-18 19:00:00", custom=[], until_date = "2019-10-19 23:59:59" , limit=1000)