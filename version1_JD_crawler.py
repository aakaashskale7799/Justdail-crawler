# importing the modules
#https://www.justdial.com/Agra/Readymade-Garment-Retailers

#https://www.geeksforgeeks.org/extract-data-from-justdial-using-selenium/

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
nameList = []
addressList = []
numbersList = []
# driver.get method() will navigate to a page given by the URL address
for i in range(1,21):
    link="https://www.justdial.com/Mumbai/Home-Loans/nct-10250496/"+"page-"+str(i)
    print(link)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    # the user-defined function
    def strings_to_num(argument):
    	
    	switcher = {
    		'dc': '+',
    		'fe': '(',
    		'hg': ')',
    		'ba': '-',
    		'acb': '0',
    		'yz': '1',
    		'wx': '2',
    		'vu': '3',
    		'ts': '4',
    		'rq': '5',
    		'po': '6',
    		'nm': '7',
    		'lk': '8',
    		'ji': '9'
    	}
    	return switcher.get(argument, "nothing")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    # fetching all the store details
    storeDetails = driver.find_elements_by_class_name('store-details')
    
    # instatiating empty lists
    
    # iterating the storeDetails
    for i in range(len(storeDetails)):
    	
    	# fetching the name, address and contact for each entry
    	name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
    	address = storeDetails[i].find_element_by_class_name('cont_sw_addr').text
    	contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
    	
    	myList = []
    	
    	for j in range(len(contactList)):
    		
    		myString = contactList[j].get_attribute('class').split("-")[1]
    	
    		myList.append(strings_to_num(myString))
    
    	nameList.append(name)
    	addressList.append(address)
    	numbersList.append("".join(myList))
    	
    # initialize data of lists.
    data = {'Company Name': nameList,
    		'Address': addressList,
    		'Phone': numbersList}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    #print(df)
    print("="*50)
    print(link[-6:])
    print("="*50)
    # Save Data as .csv
    driver.close()
df.to_csv(str(link[-6:])+'.csv', mode = 'a', header = False)