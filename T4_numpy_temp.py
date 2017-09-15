import sqlite3
import openpyxl
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook('WorldTemperature.xlsx')
wb.create_sheet("Comparison")

ws = wb.get_sheet_by_name('Comparison')
ws.cell("A1").value = "Difference"
ws.cell("B1").value = "Year"
ws.cell("C1").value = "State"
# ws["A1", "B1", "C1"] = ["Difference", "Year", "State"]

conn = sqlite3.connect("tempdb.db")
c = conn.cursor()
# c.execute("SELECT  round(avg(avgTemp),2) as yearAvgTemp, state, strftime('%Y',DATE(date)) year, strftime('%Y',DATE(date))|| state as Year_state \
#            FROM GTByState where avgTemp is not 'None' and country = 'Australia'group by Year_state order by state,year;")
# result1 = c.fetchall()
#
# c.execute("SELECT  round(avg(avgTemp),2) as yearAvgTemp, country, strftime('%Y',DATE(date)) year \
# FROM GTByCountry \
# where avgTemp is not 'None' and country = 'Australia' \
# group by year \
# order by year;")
#
# result2 = c.fetchall()

c.execute("select round(s.yearAvgTemp -  c.yearAvgTemp,2)  as difference,  s.year, s.state\
 from (SELECT round(avg(avgTemp),2) as yearAvgTemp, state, strftime('%Y',DATE(date)) year, strftime('%Y',DATE(date))|| state as Year_state \
FROM GTByState \
where avgTemp is not 'None' and country = 'Australia' \
group by Year_state order by state, year) as s,  (SELECT  round(avg(avgTemp),2) as yearAvgTemp, country, strftime('%Y',DATE(date)) year \
FROM GTByCountry \
where avgTemp is not 'None' and country = 'Australia' \
group by year \
order by year) as c \
where s.year =  c.year \
order by s.state, s.year;")

result = c.fetchall()
rows = len(result)
for row in range(rows):
    for col in range(3):
        ws.cell(row=row+2, column=col+1).value = result[row][col]

wb.save("WorldTemperature.xlsx")