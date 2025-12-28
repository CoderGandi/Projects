#Due to time,this is gonna get straight to the point.Don't forget to make it better.
Ids=[]
dct2={}
playersList=[]
Tallies=[]
print("WELCOME TO BADMINTON SYSTEM 1.0\n(Many planned features not there but major functionality achieved)")
import bfunc
print("Please enter the number of participants")
Size=int(input("Number:"))
for i in range(Size):
    playersList.append(input())
bfunc.matchplayers(playersList)
IdHandout={}
for i in range(Size):
    IdHandout[i+1]=playersList[i]
 #Collecting Ids
for j in IdHandout.keys():
    Ids.append(j)
print(Ids)
print("Time to tally\nEnter the Id of the winning person for each match.Enter 'Done' when you're finished and leave the rest to the system")
# Fixed Input Loop
while True:
    print(f"Current Players: {IdHandout}")
    val = input("Enter winning ID (or 'Done'): ").strip()
    
    if val.lower() == "done":
        break
    
    try:
        # Convert input string to integer to match IdHandout keys
        winning_id = int(val)
        if winning_id in IdHandout:
            # Map the ID back to the Player Name for a readable leaderboard
            Tallies.append(IdHandout[winning_id])
        else:
            print("Invalid ID. Please try again.")
    except ValueError:
        print("Please enter a numeric ID or 'Done'.")

# Now pointcount will receive a list of NAMES, not IDs
leaderboard = bfunc.pointcount(Tallies)
bfunc.announce(leaderboard)
