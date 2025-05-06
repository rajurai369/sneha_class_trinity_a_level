class TreasureChest:
  
    def __init__(self, questionp, answerp, pointsp):  
        self.__question = questionp  
        self.__answer = answerp  
        self.__points = pointsp  


    def getQuestion(self):
        return self.__question

    def getAnswer(self):
        return self.__answer

    def getPoints(self):
        return self.__points

def readData():
    arrayTreasure = []

    try:
       
        with open("treasurechest.txt", "r") as file:
            while True:
                question = file.readline().strip()
                if not question:  
                    break

                answer = int(file.readline().strip()) 
                points = int(file.readline().strip())  

               
                treasureChest = TreasureChest(question, answer, points)

              
                arrayTreasure.append(treasureChest)

    except FileNotFoundError:
        print("Error: The file 'treasurechest.txt' was not found.")
    except IOError:
        print("Error: Could not read the file.")

    return arrayTreasure
