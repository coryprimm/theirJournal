from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import TypeOfTag, TheTag, WholeEntry
import bcrypt
import random, string, math, re
from bs4 import BeautifulSoup


# theirJournal/apps/main/views.py
def index(request):
    return render(request, "main/index.html" )

def indexTwo(request):
    return render(request, "main/thankYou.html")

def mainList(request):
    my_entries = WholeEntry.objects.all()
    
    
    
    for i in range (0, len(my_entries)):
        
    my_tags = TheTag.objects.all()
    
    
    for k in range (0, len(my_tags)):
        
        
    context = {
            "my_entries" : my_entries,
            "my_tags" : my_tags, 
        }
    return render(request, "main/wholeEntList.html", context)

def add_tagz_base(request):
    TypeOfTag.objects.create(the_type = "pink")
    TypeOfTag.objects.create(the_type = "green")
    TypeOfTag.objects.create(the_type = "blue")

    return redirect('/')

def add_item(request):
    if request.method == 'POST':
        if request.POST['everyThing'] == "":
            messages.error(request, "Nothing you wanted saved, saved.")
            return redirect('/')
    
        theJournal = request.POST['everyThing']
        theUnSpannedJournal = request.POST['someThing']
        
        
        soup = BeautifulSoup(theJournal, "lxml")
        wholeEntryUnTagged = WholeEntry.objects.create(entry = request.POST['everyThing'])
        
        pinkT = TypeOfTag.objects.get(the_type = "pink")
        greenT = TypeOfTag.objects.get(the_type = "green")
        blueT = TypeOfTag.objects.get(the_type = "blue")

        pink = []
        green = []
        blue = []

        pinkCreations = []
        greenCreations = []
        blueCreations = []
    
        for i in range (0, len(soup.findAll('span',{"style":"background-color: pink;"})) ):
            pink.append(soup.findAll('span',{"style":"background-color: pink;"})[i].decode_contents())
        for j in range (0, len(soup.findAll('span',{"style":"background-color: green;"})) ):
            green.append(soup.findAll('span',{"style":"background-color: green;"})[j].decode_contents())
        for k in range (0, len(soup.findAll('span',{"style":"background-color: blue;"})) ):
            blue.append(soup.findAll('span',{"style":"background-color: blue;"})[k].decode_contents())

        
        # 
        


        for m in range (0, len(pink) ):
            #create the tag in the DB
            
            # 
            
            pinkCreations.append(TheTag.objects.create(content = pink[m], wholeEntry = wholeEntryUnTagged, typeOfTag = pinkT ))

            #connect the tag to the overall Text it came from
            # wholeEntryUnTagged.theTags.add(pinkCreations[m])
            #save the addition to the overall text
            wholeEntryUnTagged.save()

            #add tag to its tag type
            # pinkT.theTypeTags.add(pinkCreations[m])
            #save the addition to the tag
            pinkT.save()

            #save all the connections of the particular tag.
            pinkCreations[m].save()

            
            
            
            
            
        
        for n in range (0, len(green) ):
            
                        #create the tag in the DB
            greenCreations.append(TheTag.objects.create(content = green[n], wholeEntry = wholeEntryUnTagged, typeOfTag = greenT ))

            #connect the tag to the overall Text it came from
            # wholeEntryUnTagged.theTags.add(greenCreations[n])
            #save the addition to the overall text
            wholeEntryUnTagged.save()

            #add tag to its tag type
            # greenT.theTypeTags.add(greenCreations[n])
            #save the addition to the tag
            greenT.save()

            #save all the connections of the particular tag.
            greenCreations[n].save()

        
        for p in range (0, len(blue) ):
            
                        #create the tag in the DB
            blueCreations.append(TheTag.objects.create(content = blue[p], wholeEntry = wholeEntryUnTagged, typeOfTag = blueT ))

            #connect the tag to the overall Text it came from
            # wholeEntryUnTagged.theTags.add(blueCreations[p])
            #save the addition to the overall text
            wholeEntryUnTagged.save()

            #add tag to its tag type
            # blueT.theTypeTags.add(blueCreations[p])
            #save the addition to the tag
            blueT.save()

            #save all the connections of the particular tag.
            blueCreations[p].save()

    return redirect('/mainEntList')


