# ADGSTUDIOS (c) 2021
# EskomAPI PyPi Module

import requests
from bs4 import BeautifulSoup

def ReturnLoadSheddingStatus():
  return requests.get('https://loadshedding.eskom.co.za/LoadShedding/GetStatus').text

def GetMunicipalities(id):
    errortext = 'Try using the number id for province in parameter to return a valid json object. 1 = Eastern Cape ,2 = Free State , 3 = Gauteng ,4 = KwaZulu-Natal, 5 = Limpopo, 6 = Mpumalanga , 7 = North West , 8 = Northern Cape, 9 = Western Cape'
    try:
      if str(id).isnumeric():
        return requests.get('https://loadshedding.eskom.co.za/LoadShedding/GetMunicipalities/?Id='+str(id)).json()
      else: 
        return errortext
    except Exception as e:
       return e + ' / {0}'.format(errortext)

def GetSuburbData(id):
    try:
      if str(id).isnumeric():
        return requests.get('https://loadshedding.eskom.co.za/LoadShedding/GetSurburbData/?pageSize=1000000&pageNum=1&id='+str(id)).json()
      else: 
        return 'no valid response'
    except Exception as e:
      return e

def GetSchedule(suburbid,provincenumber):
    try:
        req = requests.get('http://loadshedding.eskom.co.za/LoadShedding/GetScheduleM/'+str(suburbid)+'/'+str(ReturnLoadSheddingStatus())+'/'+str(provincenumber)+'/'+'1')
        data = req.text
        soup = BeautifulSoup(data)
        soup.prettify()
        days = soup.find_all("div", class_="scheduleDay")
        currentday = days[0] 
        tags = currentday.find_all('a')
        output = {}
        output['index'] = []
        output['starttime'] = []
        output ['endtime'] = []
        for index,tag in enumerate(tags):
            time = tag.text
            time = time.replace(' ','')
            time = time.split('-')
            output['index'].append(index)
            output['starttime'].append(time[0])
            output['endtime'].append(time[1])
        return output
    except Exception as e:
      return 'failed to get response'