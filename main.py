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
        self.mentorshipGroup = []

    def setCoachDetails(self, coachID, specialisation, salary):
        self.coachID = coachID
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
    
    def assignMentee(self, member): 
        self.mentees.append(f"{member.name} ({member.sport})")
        print(f"Coach {self.name} is now mentoring {member.name} in {member.sport}")
    
    def getMentees(self): 
        print(self.mentees)
    
    def increaseSalary(self, percentage): 
        self.salary *= float(1 + percentage/100)
        self.salary = round(self.salary, 2)

    def mentorCoach(self, coach): 
        self.mentorshipGroup.append(f"{coach.name} ({coach.specialisation})")
        print(f"Coach {self.name} is now mentoring Coach {coach.name} in {coach.specialisation}")
    
    def getMentorshipGroup(self): 
        print(self.mentorshipGroup)
    
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
        print(f"Staff {self.name} assisted {member.name} in resolving an issue. ")

    def getStaffSum(self): 
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contactNumber}")
        print(f"Staff ID: {self.staffID}, Position: {self.position}, Years of Service: {self.yearsOfService}")

daniel = Member("Daniel", 16, "023754723057", "AKJSD346", "Football")
john = Member("John", 20, "8327618", "UGGF42356", "Basketball")
parthiv = Coach("Parthiv", 17, "283748034", "DAHFG3845", "Football", 100000)
ali = Coach("Ali", 17, "283423478", "KASDH219834", "Basketball", 10000)
junaid = Staff("Junaid", 17, "234765405", "SDJFH23984", "Teacher", 5)

parthiv.assignMentee(daniel)
john.addPerformanceScore(10)
john.addPerformanceScore(10)
john.addPerformanceScore(5)
john.addPerformanceScore(5)
john.addPerformanceScore(20)
john.calculateAverageScore()
junaid.assistMember(daniel)
ali.increaseSalary(15)
junaid.incrementYearsOfService()
daniel.getMemberSum()
john.getMemberSum()
parthiv.getCoachSum()
ali.getCoachSum()
junaid.getStaffSum()

parthiv.mentorCoach(ali)
parthiv.assignMentee(daniel)

parthiv.getMentorshipGroup()
parthiv.getMentees()