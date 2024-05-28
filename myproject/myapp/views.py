from django.shortcuts import render

from joblib import load
model=load('./model/career_model.joblib')

# Create your views here.
def index(request):
   return render(request,'index.html')
def input(request):
   return render(request,'input.html')


def DropDown(request):
   if request.method == 'POST':
      FundamentalSelect = int(request.POST['fundamentalValue'])
      ComputerSelect = int(request.POST['computerValue'])
      distributeSelect = int(request.POST['distributeValue'])
      cyberSelect = int(request.POST['cyberValue'])
      networkSelect =int (request.POST['networkValue'])
      softDevSelect =int (request.POST['softDevValue'])
      skillSelect = int(request.POST['skillValue'])
      projectSelect = int(request.POST['projectValue'])
      forensicSelect = int(request.POST['forensicValue'])
      technicalSelect = int(request.POST['technicalValue'])
      aiSelect = int(request.POST['aiValue'])
      softwareSelect = int(request.POST['softwareValue'])
      businessSelect = int(request.POST['businessVlaue'])
      communicationSelect = int(request.POST['communicationValue'])
      dataSelect = int(request.POST['dataValue'])
      troubleshootSelect =int (request.POST['troubleshootValue'])
      graphicSelect =int (request.POST['graphicValue'] 
)

      arr=[FundamentalSelect,ComputerSelect,distributeSelect,cyberSelect,networkSelect,softDevSelect,skillSelect,projectSelect,forensicSelect,technicalSelect,aiSelect,softwareSelect,businessSelect,communicationSelect,dataSelect,troubleshootSelect,graphicSelect]
      y_pred=model.predict([arr])
      for i in y_pred:
         job=i
         break
      return render(request, 'output.html',{'result':(job)})
