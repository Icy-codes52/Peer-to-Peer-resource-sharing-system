# Peer-to-Peer-resource-sharing-system
A student-focused platform for sharing and lending items among college peers, helping reduce unnecessary purchases and promote resource sharing.
—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
Readme.md
Project Title: Peer-To-Peer Resource Sharing System
 
 
By: Bhavya Bhardwaj

————————————————————————————————————————————————————————-
Overview
It is a resource-sharing platform for college students which has been developed using Python; it lets students put up the items they own (for example books, lab equipment or personal possessions) and enables other people to lend or borrow them. The system aims to encourage cooperation and make the most of resources among the members of the campus community.
 
 
 
Features
• You can add new items to the shared list.
• View Items: This displays all the items that are available in the system.
• Items can be lent, this causing the item to be taken off the list.
• There is an option to exit the program in a graceful manner.
• Error handling ensures that items which are not available are not lent and deals with invalid inputs.
 
 
 
 
Technologies & Tools used
 
• Language: Python 3.14.5
• Concepts Applied: Lists for item storage
• Control flow (if-elif-else)
• Input/output handling
• Looping (for loop with break conditions)
• Version Control: Git & GitHub
 
 

Steps to Install and Run
 
• Clone the repositories
https://github.com/Icy-codes52/Peer-to-Peer-resource-sharing-system
 
• Navigate to the project folder
cd  Bhavya
 
• Run the program
Main.py
 

 
Usage
 
When you run the program you will see a menu, with options:
Press 1 to add an item.
Enter the name of the item. The item will be added to the list.
Press 2 to view all items and lend an item.
The system displays all items.
Press 3 to lend an item, which removes the item from the list.
Press 4 to exit lending mode.
Press 999 to exit the program.
 
 
Testing Instructions
• Add an item: Add a new item (such as book, pen etc.) and check if it appears in the list.
• Lend item test: lend an item and check if it is removed from the list.
• Invalid item test: try to lent and item which is not in the list (system should reject).
• Exit test: pressing 999 to exit.
 
 
 
 
 
 
Future Enhancements
Here, the input from the user:
➢ Use a while loop that runs forever so the interaction keeps going.
➢ Make sure users are verified before they can share anything.
➢ Connect to a database so data stays saved when the program is not running.
➢ Create a graphical user interface or a web page to make it easier to use.
 
