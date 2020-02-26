import twint


def get_twitts(hashtag, file_name, since_date, until_date, format = '', limit = 100, custom = []):    
    c = twint.Config()
    if format:
        c.Format = format
    if len(custom):
        c.Custom['tweet']= custom
    c.Search = hashtag 
    c.Store_csv = True
    c.Since = since_date
    c.Until = until_date
    c.Limit = limit
    c.Output = file_name
    c.Links = False
    twint.run.Search(c)
    #c.Lang = "es"


custom_retrieve = ['date', 'timezone', 'user_id', 'username', 'tweet', 'hashtags', 'geo', 'source']

get_twitts('chile', 'test_data.csv', since_date = "2019-10-18 19:00:00", custom=custom_retrieve, until_date = "2019-10-19 23:59:59" , limit=10000)
