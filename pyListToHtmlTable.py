skills = [ 'Travis CI',
'Scrum',
'Agile Methodologies',
'Project Management',
'Software Development',
'Object-Oriented Programming (OOP)',
'Software Design',
'Data Structures',
'Algorithms',
'Analytical Skills',
'Data Analysis',
'Python (Programming Language)',
'JavaScript',
'PHP',
'MySQL',
'SQLite',
'Cascading Style Sheets (CSS)',
'HTML5',
'Linux',
'Windows',
'Git',
'GitHub',
'Selenium',
'Kivy',
'JSON',
'Angular Command Line Interface (CLI)',
'React.js',
'Angular',
'Node.js',
'Organization Skills',
'Problem Solving',
'Teamwork',
'Critical Thinking',
'Communication',
'Easily Adaptable',
'Decision-Making',
'English',
'Natural Language Processing (NLP)',
'Public Key Cryptography',
'Dynamic Programming',
'Express',
'Interpersonal Skills',
'Ionic Framework',
'Apache Cordova',
'Responsive Web Design',
'Mobile Application Development',
'System Deployment',
'Bootstrap',
'Flexbox']


skill = input('enter a skill:')
def main():
	def writeSkills():
		with open('skills.html', 'w') as a:
			for i in skills:
				a.write("<tr>" + '\n' + '\t' + "<td>" + i + "</td>" + '\n' +"</tr>" + '\n' )
			a.close()

	def checkSkills():
		for i in skills:
			if i == skill:
				print(i + ' already exists in skills')
				continue
			else: skills.append(skill)
main()

