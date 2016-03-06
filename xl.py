import xlrd
import webbrowser
import datetime
from sys import argv
script , startRow = argv #Enter exact start row from which new entries are added in .xslx file
new =2

datafile = "file.xlsx"

def parse_file(datafile=datafile):
	workbook = xlrd.open_workbook(datafile)
	sheet= workbook.sheet_by_index(0)
	title_col = 1
	type_col = 2
	link_col = 3
	date_col = 4
	events = []
	case = -1
	agree = ''
	
	data = [[sheet.cell_value(r,col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
	
	for row in range(int(startRow)-1,sheet.nrows):
		title = sheet.cell_value(row,1)
		etype = sheet.cell_value(row,2)
		link = sheet.cell_value(row,3)
		date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(row,4),workbook.datemode))
		dateString = date.strftime("%a, %d %b")
		#date=sheet.cell_value(row,4)
		dict = {'title':title,'type':etype,'link':link,'date':dateString}
		events.append(dict)
		print "New event appended"
		print " Event name: %s \n Type : %s \t link : %s  \n date : %r" %(dict['title'],dict['type'],dict['link'],dict['date'])
		print "Do you want to view the linnk? y/n"
		agree = raw_input("--> ")
			
		if agree=='y'or agree=='Y':
			if (not webbrowser.open(dict['link'],new=new)):
				print "Failed to open"
		
		case = int(raw_input("1 -- pass \t 2 -- reject \t 0 -- quit \n --> "))
		if case==1:	
			pass
		if case==2:
			del events[-1]
			print "Event removed"
		if case==0:
			break
	print "Finished all the events"
	print "Appending to the file"
	
	file = open("data.txt",'w')
	file.write(str(events))
	file.close()
	return events
	
parse_file(datafile)
		
		
	
	

