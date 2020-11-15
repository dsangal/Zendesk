import requests
import textwrap

auth = 'sangalderyk@gmail.com', 'deryk912'
GLOBALURL = 'https://sangalgroup.zendesk.com/api/v2/tickets'

def getData(url, user_input):
    if user_input == 1:
        try:
            response = requests.get(url, auth=auth)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:",errh)
            exit()
        except requests.exceptions.Timeout as errt:
            print("Timeout error: ", errt)
            exit()
        except requests.exceptions.TooManyRedirects as errr:
            print("URL error: ", errr)
            exit()
        except requests.exceptions.RequestException as e:
            print("Error occurred: ", e)
            exit()
    if user_input == 2:
        try:
            response = requests.get(url, auth=auth)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:",errh)
            exit()
        except requests.exceptions.Timeout as errt:
            print("Timeout error: ", errt)
            exit()
        except requests.exceptions.TooManyRedirects as errr:
            print("URL error: ", errr)
            exit()
        except requests.exceptions.RequestException as e:
            print("Error occurred: ", e)
            exit()
       
def printTickets():
    url = GLOBALURL + '.json?page[size]=25'
    data = getData(url, 1)
    page_num = 1
    while data:   
            print('ID  Created at                Type   Subject                                            Status     Priority      Description')
            for ticket in data['tickets']:
                print(f'{ticket["id"] : <{3}}',f'{ticket["created_at"] : <{20}}','%9s' %ticket["type"], ' ', f'{ticket["subject"] : <{50}}', f'{ticket["status"] : <{6}}','     ','%6s' % ticket["priority"],'    ', textwrap.shorten(ticket['description'],width=70))
            
            if page_num == 1:
                cont = input("Next(n): ")
            else:  
                cont = input("Previous (p) or Next (n): ")
            
            if cont == 'n':
                if data['meta']['has_more']:
                    next_url = data['links']['next']
                    data = getData(next_url, 1)
                    page_num += 1
                else:
                    data = None
                    print('That was the last of the tickets\n')
                    break
            elif cont == 'p' and page_num != 1:
                prev_url = data['links']['prev']
                data = getData(prev_url, 1)
                page_num -= 1
            else:
                print('Invalid input. Reprinting first 25 records: ')

def printOneTicket():
    user_ticketID_input = input('\nEnter an ID\n')
    print('')
    url = GLOBALURL + '/{}.json?include=users'.format(user_ticketID_input)
    data = getData(url, 2)
    description_without_breaks = data['ticket']['description'].replace('\n',' ')
    print('ID #{} | Type: {} | Subject: {}. | Created at: {} | Status: {} | Priority: {}'.format(f'{data["ticket"]["id"] : <{3}}', data["ticket"]["type"],f'{data["ticket"]["subject"] : <{20}}',f'{data["ticket"]["created_at"] : <{20}}', data["ticket"]["status"], data["ticket"]["priority"]))
    print('')
    print('Description: {}'. format(description_without_breaks))
    print('')
    print('Requested by: {} | Name: {}'.format(data['ticket']['requester_id'], data['users'][0]['name']))
    print('')
    
def programQuit():
    print("Thank you for using the ticket viewer! Good bye!")
    exit()

if __name__ == '__main__':
    user_input = ''
    while(user_input != 'quit'):
        user_input = input('menu:\n Press 1 to view all tickets\n Press 2 to view a ticket\n Type "quit" to quit\n')
        if user_input == '1':
            printTickets()
        elif user_input == '2':
            printOneTicket()
        elif user_input == 'quit':
            programQuit()
        else:
            print('Invalid input. Try again')
 
