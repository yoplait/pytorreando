class Employee(object):
    def __init__(self, name, salary, dept, company):
        self.name = name
        self.salary = salary
        self.dept = dept
        self.company = company

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.name,self.salary,self.dept,self.company)


def create_employee(name, salary, dept, company='ABC Inc.'):
    #print 'exec'
    return Employee(name, salary, dept, company)


#create two employees

e1 = create_employee('Bob',56878,'HR')
e2 = create_employee('tuputamadre',3434343,'Puta',)
e3 = create_employee(company='xyz', name='pepa',dept='salidas',salary=3434343)

print 'start'
print e1
print e2
print e3
print 'end'
print e1.salary
