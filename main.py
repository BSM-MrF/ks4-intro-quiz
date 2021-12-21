def loadFile(name):
    try:
        with open(name,"rt") as file:
            # getQuestions(file)
            questions = []
            for line in file:
                # print("** " + line)
                split = line.split(';')
                questions.append(split)
        return questions
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Another error!")
        # return False

def printQuestions(questions):
    for i in range(0,len(questions)):
        # Using a 'f-string' to easily include variables in a string
        print(f"Question {i+1}:")
        print(questions[i][0])
        for j in range(1,len(questions[i])):
            print(j,"-",questions[i][j])
        # Using 'f-strings' to include variablesin the string when printing.
        # print(f"Q{i+1}: {questions[i][0]}")
  

#*** __MAIN__ ***#
questions = loadFile("data/data.txt")
if questions != None:
    printQuestions(questions)
