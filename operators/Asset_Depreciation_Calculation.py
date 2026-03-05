initial_lapptop_price = 12000000
salvage_value = 2000000
Economic_life = 4
annual_depreciation = (initial_lapptop_price-salvage_value)/Economic_life
value_after_2_years = initial_lapptop_price - (annual_depreciation * 2)

print("Annual Depreciation is: ", annual_depreciation, "rupiah")
print("Value after 2 years is: ", value_after_2_years, "rupiah")