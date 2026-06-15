# create 2 csv files - sales_q1, sales_q2 with fields - product, units_sold, revenue
# create a sales_semi_annual.csv by combining the 2 quarter sales files. Add a new column called quarter.
# create a summary report

from csv import DictReader, DictWriter
from collections import defaultdict

# sample data
q1_data = [
    {'product': 'P001', 'units_sold': 120, 'revenue': 2400},
    {'product': 'P002', 'units_sold': 80, 'revenue': 2600},
    {'product': 'P003', 'units_sold': 85, 'revenue': 4250}
]

q2_data = [
    {'product': 'P002', 'units_sold': 80, 'revenue': 2600},
    {'product': 'P003', 'units_sold': 85, 'revenue': 4250},
    {'product': 'P004', 'units_sold': 150, 'revenue': 5500}
]

def write_to_csv(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = DictWriter(f, fieldnames=['product', 'units_sold', 'revenue'])
        writer.writeheader()
        writer.writerows(data)

write_to_csv('sales_q1.csv', q1_data)
write_to_csv('sales_q2.csv', q2_data)

# combines the 2 csv files
combined_sales = []

for filename, quarter in [('sales_q1.csv', 'Q1'), ('sales_q2.csv', 'Q2')]:
    with open(filename, 'r', encoding='utf-8') as f:
        for row in DictReader(f):
            row['quarter'] = quarter
            combined_sales.append(row)

# write the combined csv
with open('sales_semi_annual.csv', 'w', encoding='utf-8', newline='') as f:
    writer = DictWriter(f, fieldnames=['product', 'units_sold', 'revenue', 'quarter'])
    writer.writeheader()
    writer.writerows(combined_sales)

# revenue summary
totals = defaultdict(float)
for row in combined_sales:
    totals[row['product']] += float(row['revenue'])

# summary report
print('Summary Report\n')
for product, total in sorted(totals.items(), key=lambda x: -x[-1]):
    print(f' {product:12}: Rs.{total:,.0f}')