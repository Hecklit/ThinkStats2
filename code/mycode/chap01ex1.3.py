import pandas

df = pandas.read_stata('../data/ESS7DE.dta', convert_categoricals=False, convert_missing=True)
print(df.columns.values)
print(df.edufde2.value_counts()) # EDUFDE2