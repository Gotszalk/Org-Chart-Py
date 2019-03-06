from string import Template
import csv


def loadStructure(csvfile):
	structure = []
	#load csv data
	with open(csvfile, 'rb') as csvpntr:
			csvreader = csv.reader(csvpntr, delimiter=',')
			for row in csvreader:
						structure.append(row)
	return structure

def findChildren(parent, structure):
	
	children =[]
	for employee in structure:
		if employee[2] == parent:
			children.append(employee)
	return children
	
def generateLevel(parents, structure):
	
	content = ""
	
	for parent in parents:
			children = findChildren(parent[0], structure)
						
			content += """<li><div>""" + parent[0] + "<br />" + parent[1] + '</div>'
			
			if len(children)>0:
				#recurence if there are children
				content += """
				<ol>""" + generateLevel(children, structure) + """
					</ol>
					"""
	return content

def writeResult(chart):
	x = open("templateA.html", 'r')
	template = x.read()
	#template.format(zm = "cos")
	result = open("result.html", 'w')
	result.write(template.format(content = chart))

structure = loadStructure('structure.csv')
uberfather = findChildren('1', structure)
chart = generateLevel(uberfather, structure)
#print("oto i ten wygenerowany html: xx = chart)
writeResult(chart)

