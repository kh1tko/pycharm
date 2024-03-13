class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('owner'), float(doc.findtext('amount')))


# Пример использования
data = '''
<account>
<owner>Guido</owner>
<amount>1000.0</amount>
</account>
'''
a = Account.from_xml(data)
print(a.owner)
print(a.balance)
