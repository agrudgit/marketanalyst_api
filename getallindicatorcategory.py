import marketanalyst
client = marketanalyst.client("2c3f12-0e5e01-57556e-58628f-6", "eb5a1d-a34be0-cfe29a-267718-254bad-3b")
df = client.getallindicatorcategory()
print(df.to_string(index=False))
