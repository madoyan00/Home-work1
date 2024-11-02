import os, json
from pprint import pp

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

newChessPlayers = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]


newChessPlayer = {'id': 34, 'name': 'Joblik', 'country': 'Georgia', 'rating': 2888, 'age': 51}

def createfile():
    try:
        os.mkdir("files")
        print("file is created!")
    except:
        print("file was created!")

createfile()

print("-" * 165)
# 1
def createFileInFile():
    try:
        with open("files/test.json", mode="x", encoding="utf-8" ) as file:
            print("test.json is created!")
    except:
        print("test.json was created!")

createFileInFile()

print("-" * 165)
# 2
def writeFile(path, jsonData):
    with open(path, mode="w", encoding="utf-8") as file:
       file.write(json.dumps(jsonData, indent=2))
writeFile("files/test.json", chess_players)

def readFile(path):
        with open(path, mode="r", encoding="utf-8") as file:
            return json.loads(file.read())
pp(readFile("files/test.json"))
print("-" * 165)
# 3
def updateFile(path, jsonData):
  data = readFile(path)
  data.append(jsonData)
  return data

data1 = updateFile("files/test.json",newChessPlayer)


def writeFile(path, jsonData):
    with open(path, mode="w", encoding="utf-8") as file:
       file.write(json.dumps(jsonData, indent=2))
writeFile("files/test.json", data1)

print("-" * 165)
# 4
def updateFile1(path, jsonData):
  data = readFile(path)
  for players in newChessPlayers:
      data.append(players)
  return data

data2 = updateFile1("files/test.json",newChessPlayer)

def writeFile(path, jsonData):
    with open(path, mode="w", encoding="utf-8") as file:
       file.write(json.dumps(jsonData, indent=2))
writeFile("files/test.json", data2)
print("-" * 165)