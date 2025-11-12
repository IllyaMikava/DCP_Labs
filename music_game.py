# //Part 1: Creating Basic Classes

# class Musician:
#     def __init__(self, name, instrument, skill_level):
#         self.name = name
#         self.instrument = instrument
#         self.skill_level = skill_level

#     def play(self):
#         return f"{self.name} plays the {self.instrument}"
    
#     def practice(self):
#         if self.skill_level<10:
#             self.skill_level += 1

#     def get_info(self):
#         return f"{self.name} plays {self.instrument} and he has skill level at {self.skill_level}"

# # musician1 = Musician("Aoife", "fiddle", 7)
# # print(musician1.play())
# # print(musician1.get_info())
# # musician1.practice()
# # print(musician1.get_info())

# // Part 2: Encapsulation

# class Musician:
#     def __init__(self, name, instrument, skill_level):
#         self.name = name
#         self.instrument = instrument
#         self.skill_level = skill_level

#     def play(self):
#         return f"{self.name} plays the {self.instrument}"

#     def practice(self):
#         if self.skill_level < 10:
#             self.skill_level += 1

#     def get_info(self):
#         return f"{self.name} plays {self.instrument} at skill level {self.skill_level}"


# # Session class with encapsulation
# class Session:
#     def __init__(self, location, max_capacity):
#         self.__musicians = []           # private list of Musician objects
#         self.__location = location      # private string
#         self.__max_capacity = max_capacity  # private integer

#     def add_musician(self, musician):
#         if len(self.__musicians) < self.__max_capacity:
#             self.__musicians.append(musician)
#             print(f"{musician.name} joined the session at {self.__location}.")
#         else:
#             print("Session is full! Cannot add more musicians.")

#     def remove_musician(self, name):
#         for musician in self.__musicians:
#             if musician.name == name:
#                 self.__musicians.remove(musician)
#                 print(f"{name} has left the session.")
#                 return
#         print(f"No musician named {name} found in the session.")

#     def get_musician_count(self):
#         return len(self.__musicians)

#     def list_musicians(self):
#         if not self.__musicians:
#             print("No musicians in the session yet.")
#         else:
#             print("Musicians currently in the session:")
#             for musician in self.__musicians:
#                 print(f"- {musician.get_info()}")

#     def get_location(self):
#         return self.__location

# musician1 = Musician("Aoife", "fiddle", 7)

# session = Session("The Cobblestone", 5)
# session.add_musician(musician1)
# session.add_musician(Musician("Liam", "guitar", 6))
# session.list_musicians()
# print(f"Musicians in session: {session.get_musician_count()}")



# // Part 3: Inheritance

# class Musician:
#     def __init__(self, name, instrument, skill_level):
#         self.name = name
#         self.instrument = instrument
#         self.skill_level = skill_level

#     def play(self):
#         return f"{self.name} plays the {self.instrument}"
    
#     def practice(self):
#         if self.skill_level<10:
#             self.skill_level += 1

#     def get_info(self):
#         return f"{self.name} plays {self.instrument} and he has skill level at {self.skill_level}"
    
# class LeadMusician(Musician):
#     def __init__(self, name, instrument, skill_level, speciality):
#         super().__init__(name, instrument, skill_level)
#         self.speciality = speciality
    
#     def play(self):
#         return f"{self.name} leads the session with {self.speciality} on {self.instrument}"
    
#     def start_tune(self, tune_name):
#         return f"{self.name} starts playing {tune_name}"
    
# class BeginnersMusician(Musician):
#     def __init__(self, name, instrument, skill_level):
#         super().__init__(name, instrument, skill_level)
#         self.learning = True

#     def play(self):
#         return f"{self.name} is learning to play the {self.instrument}"

#     def graduate(self):
#         self.learning = False
#         self.skill_level = min(10, self.skill_level + 2)
    
    
# lead = LeadMusician("Máire", "flute", 9, "slip jigs")
# beginner = BeginnersMusician("Tom", "bodhrán", 3)

# print(lead.play())
# print(lead.start_tune("The Butterfly"))
# print(beginner.play())
# beginner.graduate()
# print(f"{beginner.name} skill level: {beginner.skill_level}")



# // Part 4: Polymorphism

# -------------------------
# Base Class
# -------------------------
class Musician:
    def __init__(self, name, instrument, skill_level):
        self.name = name
        self.instrument = instrument
        self.skill_level = skill_level

    def play(self):
        return f"{self.name} plays the {self.instrument}"

    def practice(self):
        if self.skill_level < 10:
            self.skill_level += 1

    def get_info(self):
        return f"{self.name} plays {self.instrument} at skill level {self.skill_level}"


# -------------------------
# Subclass 1: LeadMusician
# -------------------------
class LeadMusician(Musician):
    def __init__(self, name, instrument, skill_level, specialty):
        super().__init__(name, instrument, skill_level)
        self.specialty = specialty

    def play(self):
        return f"{self.name} leads the session with {self.specialty} on {self.instrument}"

    def start_tune(self, tune_name):
        return f"{self.name} starts playing {tune_name}"


# -------------------------
# Subclass 2: BeginnersMusician
# -------------------------
class BeginnersMusician(Musician):
    def __init__(self, name, instrument, skill_level):
        super().__init__(name, instrument, skill_level)
        self.learning = True

    def play(self):
        return f"{self.name} is learning to play the {self.instrument}"

    def graduate(self):
        self.learning = False
        self.skill_level = min(10, self.skill_level + 2)


# -------------------------
# Polymorphism Demonstration
# -------------------------
def hold_session(musicians):
    print("--- Session Starting ---")
    for musician in musicians:
        print(musician.play())  # Calls the correct play() depending on the object's class
    print("--- Session Ending ---")


# -------------------------
# Test Code
# -------------------------
musicians = [
    Musician("Aoife", "fiddle", 7),
    LeadMusician("Máire", "flute", 9, "slip jigs"),
    BeginnersMusician("Tom", "bodhrán", 3)
]

hold_session(musicians)


# -------------------------
# Questions and Answers
# -------------------------

# 1️⃣ What advantages does encapsulation provide in the Session class?
# Encapsulation hides the internal details (like the musician list, location, and max capacity)
# from direct access. This prevents accidental modification and ensures that data is only changed
# through controlled methods (like add_musician or remove_musician), improving security and reliability.

# 2️⃣ How does inheritance help avoid code duplication between Musician classes?
# Inheritance allows LeadMusician and BeginnersMusician to reuse the attributes and methods
# from the Musician base class (name, instrument, skill_level, etc.) instead of rewriting them.
# They only override or extend the behavior where necessary, reducing repetition.

# 3️⃣ Give an example of polymorphism from this lab and explain why it's useful.
# The function hold_session() calls the play() method on each object.
# Even though all objects are of different types (Musician, LeadMusician, BeginnersMusician),
# Python automatically uses the correct version of play().
# This is useful because we can write generic code that works with any subclass.

# 4️⃣ What other real-world scenarios could you model using OOP?
# Examples include:
# - A school system with base class Person and subclasses Student and Teacher
# - A zoo with Animal as a base class and specific species as subclasses
# - A vehicle system with Vehicle as the base class and Car, Bus, and Bike as subclasses
# - A banking app with Account as the base class and SavingsAccount or CreditAccount subclasses



