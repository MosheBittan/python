#pyton lab 1 : Variables,Data types , lists and dictionary

####print task 1###
print("Task 1: ")

#create new empty list
serverlist = []

#for loop for get server name from user and add to list
for i in range(3):
    userServerName=input(f"Please enter the server name {i+1} : ")
    serverlist.append(userServerName)

#print the full server list
print(f"Servers: {serverlist}")


###print task 2###
print("Task 2: ")

#Define new empty dictionary variable
serversWithIP={}

for serverName in serverlist:
    print(f"Enter IP address for {serverName} :")
    serversWithIP[serverName]=input()

#Print the dictionary
print(f"Server configuration: {serversWithIP}")


###print task3###
print("Task 3:")

#Print all dictionary key and value
print(f"The servers names and IP: {serversWithIP}")

#while loop for entry value from user and print from dictionary
while True:
    userServerKey=input(f"Enter a server name to view details: (quit with q)")
    #if you enter 'q' you will exit from while loop
    if userServerKey == "q":
        break
    #get value from the key (server) the user input
    dictValue=serversWithIP.get(userServerKey)
    #if the value not equall to None means it valid in dict then print key -> value
    if dictValue != None:
        print(f"{userServerKey} has IP address {dictValue}")
    else:
        print(f"Error!!! not exist key")


##Task 4:###

userChoice=input(f"Do you want to update any server's IP address? (yes/no):")
if userChoice != "no":
    userServer=input(f"Enter the server name:")
    if serversWithIP.get(userServer) != None:
        userIP=input(f"Enter the new IP address:")
        #Set the new ip for the server choice [key=server , value=ip]
        serversWithIP[userServer]=userIP
        #print updated dict
        print(f"Updated server configurations: {serversWithIP}")
    else:
        print("The server name you have entered not exist!")

print("Goodbye!!!!!")