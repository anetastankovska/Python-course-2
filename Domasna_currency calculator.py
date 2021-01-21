
import requests

# https://api.exchangeratesapi.io/latest




class Calculator:
    
    def get_rate(self, currency, base):
        raw_rate = requests.get("https://api.exchangeratesapi.io/latest?base="+str(base).upper()).json()
        rate = raw_rate["rates"][currency]
        return rate
    
    
    def calculate_to_currency(self, from_currency, to_currency, amount):
        
        rate = self.get_rate(to_currency, from_currency)
        return amount * rate
        
        
    
calc = Calculator()    
miro = calc.calculate_to_currency("USD", "GBP", 100)
print(Calculator().calculate_to_currency("CAD", "USD", 100))
print(miro)


    

