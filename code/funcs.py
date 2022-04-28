from sklearn.preprocessing import LabelEncoder, StandardScaler

def dec_tree(df, dat_type):
    data = df.drop(['id', 'tid1', 'tid2'], axis=1)
    x = data[:, :-1]
    y = data[:, -1]
    
    encoder = LabelEncoder()
    encoder.fit_transform(x)
    
    scaler = StandardScaler()
    scaler.fit_transform(x)