class Madlib:

  adj = input("Adjective: ")
  verb = input("Verb: ")
  famous_person = input("Famous Person: ")

  line = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb}. Stay hydrated like you are {famous_person}"
  
  def printMadlib(self,line):
      print(line)

madlib1 = Madlib()

madlib1.printMadlib(madlib1.line)

