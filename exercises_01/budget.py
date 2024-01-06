# Given income and single person tax allowance
income = 135000
single_person_tax_allowance = 40100

# Calculating the taxable income at 20% tax rate
taxable_at_20_percent = income - single_person_tax_allowance

# Calculating the taxable income at 40% tax rate
taxable_at_40_percent = income - taxable_at_20_percent

# Calculating the tax amount at 20% and 40% rates
percent_tax_20 = taxable_at_20_percent * 0.2
percent_tax_40 = taxable_at_40_percent * 0.4

# Summing up the total tax
total_tax = percent_tax_20 + percent_tax_40

# Displaying the total tax
print("Total Tax:", total_tax)
