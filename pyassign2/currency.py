#------------------------------currency------------------------------#
#------------------------------Diana_Yu------------------------------#
#------------------------------20171203------------------------------#
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

from urllib.request import urlopen
    
def exchange(currency_from, currency_to, amount_from):
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    idxpun1=jstr.find(':')
    idxpun2=jstr.find(':',idxpun1+1)
    idxspa=jstr.find(' ',idxpun2+2)
    amount_to=float(jstr[idxpun2+3:idxspa])
    return amount_to

#----------------------------testcurrency----------------------------#
"""Unit test for module currency

When run as a script, this module invokes several procedures that 
test the various functions in the module currency."""
def testA():
    assert(exchange('USD','EUR',2.50)==2.0952375)

def testB():
    assert(exchange('EUR','USD',5)==5.9659107857701)

#-------------------------------testal-------------------------------#
"""Unit test for module testcurrency

When run as a script, this module invokes several procedures that 
test the various functions in the module currency."""
def testAll():
    testA()
    testB()
    
testAll()

#----------------------------input&output------------------------------#
"""Moduld for get the input and print the output"""

currency_from=input('the currency on hand')
currency_to=input('the currency to convert to')
amount_from=float(input('amount of currency to convert'))

print(exchange(currency_from, currency_to, amount_from))