fifteen_new_employees = "Bob Howard Ryan John Matthew Yolandi Mitchell James Todd"

print "You are missing some employees names in the list. There are only nine,"
print "so you will need to add another six names. Let's do it!"

employees = fifteen_new_employees.split(' ')

missing_employees = ["Roger", "Rebecca", "Vivian", "Jason", "Mars", "Pluto"]

while len(employees) != 15:
    extra_names = missing_employees.pop()
    print "Missing employee ", extra_names
    employees.append(extra_names)
    print "You have now added all %d employees. Good job!" % len(employees)

print "Here are some cool manipulations you can manuever ", employees

print employees[10]

print employees [-8]

print employees.pop()

print ' '.join(employees)

print ' cannot stand '.join(employees[0:15])
