print(""" 4TH INDUSTRIAL REVOUTION 

the 4th Industrial revolution is blah blah 

-MENU- 
'''''

Please choose one of the options below, and press enter. 

1) Question & Answer 1
2) Question & Answer 2
3) Question & Answer 3
""")

answer = "empty"


while(answer == "empty"):
  userchoice = input("your choice: ")
  answer = "chosen"
  
  if(int(userchoice) == 1):
    print("""QUESTION 1:  Why are you here at school?
    
    ANSWER 1:I am here because I do not want to be disappointed and poor. I do want to learn, but I feel like in the system setup in schools today that is not what I am getting out of it. I wish there was a way to have curriculum work more around each student but still be able to teach thousands without there being too much work on teachers.  """)
  elif(int(userchoice) == 2):
    print("""QUESTION 2: What is the purpose of school?

ANSWER 2:The purpose of school is to build good employees to fill the gaps in the capistilitic structure of our patriarchal society. The true purpose of school is to educate and help people learn, but I feel that as time goes on schools are turning more and more into prisons with things like metal detectors, numbers by which students get to do things, literally police officers on campus, controlling of when and where students get to move out of safety and not for the purpose of more organized learning. It makes me sad. 
 """)
  elif(int(userchoice) == 3):
    print("""QUESTION 3:Are you getting out of it, what you should be getting out of it?

 ANSWER 3:  NO I AM STILL HERE, I am not getting as much out of it as i should. I know that there aren't that many other places with that higher education that would not cost an arm, a leg, and a kidney which is awful, Though I am getting some leadership opportunities here that are not through the school but the work of my teachers.  I should be learning, but some people are holding us back (not me). I know on some level that I would get more out of school if I had more choices. I think we should have more choices in school because I should be learning and getting an education that can help my future. I know a lot of my peers will never use logarithmic equations again because they can not afford further university education to get to a level where it is necessary and putting them through that now does not feel necessary to have them prepare and learn for THEIR future. 
 """)
  else:
    print("INVALID INPUT, please try again ")
    answer = "empty"
