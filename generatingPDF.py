fruit = {
    "Apple": 2,
    "Bananas": 1,
    "Cherries": 5,
    "Grapes": 10,
    "Elderberries": 1
}
from msilib.schema import tables
from reportlab.platypus import SimpleDocTemplate

report = SimpleDocTemplate("assets/report.pdf")

from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# build pdf
# report.build([report_title])

# creating tables 

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# print(table_data)
# report_table = Table(data=table_data)
# report.build([report_title, report_table])

# setting table design
from reportlab.lib import colors
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.blanchedalmond)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
# report.build([report_title, report_table])

# now drawing graph 
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

report_pie = Pie(width=3*2, height=3*2)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

print(report_pie.data)
print(report_pie.labels)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])
