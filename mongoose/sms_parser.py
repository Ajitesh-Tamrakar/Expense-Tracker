from mongoose.models import raw_data
import re 


class SMSParser:
    def __init__(self, sms):
        self.sms = sms
        self.data = {}
        self.amount_extractor()
        # self.transaction_type()
        # self.party()
        # self.transaction_method()
        # self.transaction_id()
        # self.date()
    def amount_extractor(self):
        pattern = r"Rs.\s?(\d*\.?\d*)"
        match  = re.search(pattern, self.sms)
        if match:
            amount =float(match.group(1))
            self.data['amount'] = amount          
            
        else:
            self.data['amount'] = 'not found'
    def transaction_type(self):
        pattern = r'Rs.\s?\d*\.?\d*\sfrom\s|\sdebited\s'
        match = re.search(pattern, self.sms)
        if match:
            self.data['type'] = "Debit"
        else:
            self.data['type'] = 'Not Found'
            
    def party(self):
        pattern = r'(?:Rs.\s?\d*\.?\d*\sfrom\s|\sdebited\s\w*/?c?\w*\sand\scredited\sto\s)(.*)via'
        match = re.search(pattern, self.sms)
        if match:
            if self.data['type'] == 'Debit':
                self.data['recipient'] = match.group(1)
            elif self.data['type'] == 'Credit':
                self.data['sender'] = match.group(1)
        else:
            self.data['party'] = 'not found'
            r''
    # def transaction_method(self):
    #     pattern = r'UPI'
    #     match = re.search(pattern, self.sms)
    #     if match:
    #         self.data['mode'] = 'UPI'
    # def transaction_id(self):
    #     pattern = r'Ref No (\d*) on'
    #     match = re.search(pattern, self.sms)
    #     if match:
    #         self.data['Transaction ID'] = match.group(1)
    # def date(self):
    #     pattern = r'on (\w*).'
    #     match = re.search(pattern, self.sms)
    #     if match:
    #         self.data['Date'] = match.group(1)
    def output(self):
        return self.data