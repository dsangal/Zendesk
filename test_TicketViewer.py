import unittest
from TicketViewer import getData
from builtins import str

class TestTicketViewer(unittest.TestCase):
    def test_getData_printTix(self):
        self.assertGreater(str(getData('https://sangalgroup.zendesk.com/api/v2/tickets.json?page[size]=25',1)).find("tickets"), 0)  
    def test_getData_printTix_checkField(self):
        self.assertGreater(str(getData('https://sangalgroup.zendesk.com/api/v2/tickets.json?page[size]=25',1)).find("created_at"), 0)  
    def test_getData_requestID_checkField(self):
        self.assertGreater(str(getData('https://sangalgroup.zendesk.com/api/v2/tickets/2.json?include=users',2)).find("name"), 0)
    def test_getData_requestID_checkTick(self):    
        self.assertGreater(str(getData('https://sangalgroup.zendesk.com/api/v2/tickets/2.json?include=users',2)).find("ticket"), 0)
        
if __name__ == '__main__':
    unittest.main()
        
