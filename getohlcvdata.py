import marketanalyst
client = marketanalyst.client("2c3f12-0e5e01-57556e-58628f-6", "eb5a1d-a34be0-cfe29a-267718-254bad-3b")
df = client.getOHLCVData(["NASDAQ:AAPL", "NASDAQ:MSFT"], "2019-01-01", "2019-01-15",)


client.export_df(df, 'csv', "aapl")
print( df)
