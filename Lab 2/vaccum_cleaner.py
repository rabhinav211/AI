
class room:

    def __init__(self,a):
        self.state=a
    def suck(self):
        self.state="clean"
    
n=2
roomList=[]
for i in range(n):
    a=str(input(f"Enter room {i+1} state:"))
    roomList.append(room(a))
start=int(input("Enter starting room number:"))-1

print("Before cleaning")
print("Room\tState")
for i in range(len(roomList)):
    print(f"{i+1}\t{roomList[i].state}")

count=0
while count<len(roomList):
    if(roomList[start].state.lower()=="dirty"):
        roomList[start].suck() 
    start=(start+1)%len(roomList)
    count+=1

print("\n")
print("After cleaning")
print("Room\tState")

for i in range(len(roomList)):
    print(f"{i+1}\t{roomList[i].state}")
