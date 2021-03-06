class AddressBook:
	
	person_list = []
	
	def add(self, person):
		self.person_list.append(person)
	
	def show_all(self):
		for person in self.person_list:
			print(person.lastname + " " + person.firstname)
			
	def search(self, keyword):
		for person in self.person_list:
			if keyword in person.firstname or keyword in person.lastname:
				print(person.firstname + " " + person.lastname)
				
class Person:
	import datetime
	
	firstname = ''
	lastname = ''
	tel = ''
	maiL_address = ''
	birthday = datetime.datetime(2000, 1, 1)
	
ab = AddressBook()

p = Person()
p.firstname = 'michitaka'
p.lastname = 'yumoto'
p.tel = '090-1234-5678'

ab.add(p)

p2 = Person()
p2.firstname = 'John'
p2.lastname = 'Lennon'
p2.tel = '080-1234-5678'

print('---check---')
ab.add(p2)

print('add_num' + str(len(ab.person_list)) + 'nin')

print('---view---')
ab.show_all()

print('---search---')
ab.search('John')

			
