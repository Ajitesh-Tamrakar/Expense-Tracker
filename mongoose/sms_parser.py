import re 
class SMSParser:
    def __init__(self, sms):
        self.sms = sms
        self.data = {}
        self.amount_extractor()
        self.transaction_type()
        self.Bank_wise_filter()
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
            
    def Bank_wise_filter(self):
        if 'BOI' in self.sms: 
            amount_pattern = r'(?:Rs.\s?\d*\.?\d*\sfrom\s|\sdebited\s\w*/?c?\w*\sand\scredited\sto\s)(.*)via'
            date_pattern = r'debited.*on (\w*).'
            transaction_mode_pattern = r"(?:Rs.\s?\d*\.?\d*\sfrom\s|\sdebited\s\w*/?c?\w*\sand\scredited\sto\s).*via\s(UPI)"
        elif 'HDFC' in self.sms:
            amount_pattern = r'Sent.*To\s(.*)\sOn'
            date_pattern = r'Sent.*From\sHDFC\sBank.*On\s(.*)\sRef'
            transaction_mode_pattern = r'Sent.*From\sHDFC\sBank.*BLOCK\s(UPI)'
        elif 'Kotak Bank' in self.sms:
            amount_pattern = r'Sent.*to\s(.*)on'
            date_pattern =r'Sent.*to\s.*on\s(.*).U'
            transaction_mode_pattern = r'Sent.*from Kotak Bank.*(UPI)'
        else:
            print('Bank not found')
            
        amount_match = re.search(amount_pattern, self.sms)
        date_pattern_match = re.search(date_pattern, self.sms)
        transaction_mode_pattern_match = re.search(transaction_mode_pattern, self.sms)
        if amount_match:
            self.data['Amount'] = amount_match.group(1)
        if date_pattern_match:
            self.data['Date'] = date_pattern_match.group(1)
        if transaction_mode_pattern_match:
            self.data['Mode'] = transaction_mode_pattern_match.group(1)
            
    
    def output(self):
        return self.data