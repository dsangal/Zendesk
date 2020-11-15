# Zendesk coding challenge

Zendesk Ticket Vieweris a customer service tool that allows the creation and management of support tickets.

## Installation:

Download Python3

## Usage:

1. Open terminal and go to the location of the files.

2. Run TicketViewer.py on the terminal

    > python3 TicketViewer.py
    
3.  TicketViewer.py will displays the following menu items:

	menu:
	 	Press 1 to view all tickets
	 	Press 2 to view a ticket
	 	Type "quit" to quit

4. If menu item 1 is entered, the application will display all the tickets using pagination by displaying 25 ticket at a time.

	To see more tickets beyond first page, enter ’n’ to view next page.
        To go back to the previous page, enter ‘p’.
	
	The following ticket information is displayed on the ticket list:
	- Ticket ID  
	- Created at
	- Type
	- Subject
	- Status     
	- Priority      
	- Description

5.  If menu item 2 is entered, applicaiton will ask for the ID of the requested ticket.  
    
    	The following detailed ticket information is displayed.
	- Ticket ID  
	- Type
	- Subject
	- Created at
	- Description
	- Requested By
	- Status     
	- Priority       
	
6.  Enter "quit" to quit from the application.

7. To run unit tests, run test_TicketViewer.py on the terminal

   > python3 -m unittest  
   



