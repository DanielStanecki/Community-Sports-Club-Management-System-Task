class Person: 
    def __init__(self, name, age, contactNumber): 
        self.name = name
        self.age = age
        self.contactNumber = contactNumber
    
    def setDetails(self, name, age, contactNumber): 
        self.name = name
        self.age = age
        self.contactNumber = contactNumber

    def getDetails(self): 
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contactNumber}")
    
class Member(Person): 
    def __init__(self, name, age, contactNumber, membershipID, sport):
        super().__init__(name, age, contactNumber)
        self.membershipID = membershipID
        self.sport = sport
        self.performanceScores = []
        self.average = 0

    def setMemberDetails(self, membershipID, sport):
        self.membershipID = membershipID
        self.sport = sport

    def addPerformanceScore(self, score): 
        self.performanceScores.append(score) 
    
    def calculateAverageScore(self): 
        self.average = sum(self.performanceScores) / len(self.performanceScores)
        print(f"The average score is {self.average}")
    
    def getMemberSum(self): 
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contactNumber}")
        print(f"Membership ID: {self.membershipID}, Sport: {self.sport}, Average Performance Score: {self.average}")

class Coach(Person): 
    def __init__(self, name, age, contactNumber, coachID, specialisation, salary):
        super().__init__(name, age, contactNumber)
        self.coachID = coachID
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
    
    def setCoachDetails(self, coachID, specialisation, salary):
        self.coachID = coachID
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
    
    def assignMentee(self, member): 
        self.mentees.append(member.name)
        print(f"Coach {self.name} is now mentoring {member.name} in {self.specialisation}")
    
    def getMentees(self): 
        print(self.mentees)
    
    def increaseSalary(self, percentage): 
        self.salary *= float(1 + percentage/100)
        self.salary = round(self.salary, 2)
    
    def getCoachSum(self): 
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contactNumber}")
        print(f"Coach ID: {self.coachID}, Specialisation: {self.specialisation}, Salary: {self.salary}, Mentees: {self.mentees}")
    
class Staff(Person): 
    def __init__(self, name, age, contactNumber, staffID, position, yearsOfService): 
        super().__init__(name, age, contactNumber)
        self.staffID = staffID
        self.position = position
        self.yearsOfService = yearsOfService
    
    def setStaffDetails(self, staffID, position, yearsOfService): 
        self.staffID = staffID
        self.position = position
        self.yearsOfService = yearsOfService
    
    def incrementYearsOfService(self): 
        self.yearsOfService += 1
    
    def assistMember(self, member): 
        print(f"Staff {self.name} assissted {member.name} in resolving an issue. ")

    def getStaffSum(self): 
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contactNumber}")
        print(f"Staff ID: {self.staffID}, Position: {self.position}, Years of Service: {self.yearsOfService}")

daniel = Member("Daniel", 16, "023754723057", "AKJSD346", "Football")
john = Member("John", 20, "8327618", "UGGF42356", "Basketball")
