def pre_proc(df):
    df.drop(['title1_zh', 'title2_zh'], axis=1, inplace=True)
    df.replace(['agreed', 'disagreed'], 'related', inplace=True)