import json, codecs
from collections import defaultdict

def main():

#make some lists to contain data
    namelist = []
    comicslist2 = []
    serieslist2 = []
    eventslist2 = []
    storieslist2 = []
    #characterdict = {}
   
    
    
#read json, open appearance files, write out headers
    marvelcharacters = open('allcharacters.txt', 'rU').readlines()
    comicsfile = open('comics.txt', 'w')
    seriesfile = open('series.txt', 'w')
    eventsfile = open('events.txt', 'w')
    storiesfile = open('stories.txt', 'w')
    test = open('test.txt', 'w')
    comicsfile.write('Character' + '\t' + 'Comics' +'\n')
    #comicsfile.write('Comic Appearance' +'\n')
    seriesfile.write('Character' + '\t' + 'Series' +'\n')
    #seriesfile.write('Series Appearance' +'\n')
    eventsfile.write('Character' + '\t' + 'Events' +'\n')
    #eventsfile.write('Event Appearance' +'\n' + 'Story Appearance' +'\n')
    storiesfile.write('Character' + '\t' + 'Stories' +'\n')
    #storiesfile.write('Story Appearance' +'\n')
    
#iterate through lines, load json, iterate through key/values of outer and inner dictionary, append to list if key is a certain value    
    for lines in marvelcharacters:
        characterdata = json.loads(lines)
        for keys, values in characterdata.items():
            if keys == 'data':
                 for key, value in values.items():
                    if key == 'results':
                        for line in value:
                            characterdict = {}
                            name = []
                            comicslist = []
                            serieslist = []
                            eventslist = []
                            storieslist = []
                            for charkey, charvalue in line.items():
                                if 'name' in charkey:
                                    name.append(charvalue)
                                    character = charkey
                                    character = 'character'
#                                     if character not in characterdict:
#                                         characterdict[character] = charvalue
#                                     else:
#                                         continue
                      #           else:
#                                     #name.append('NA')
#                                     character = 'character'
#                                     characterdict[character] = 'NA'  
                                
                                if 'comics' in charkey:
                                    for comkey, comvalue in charvalue.items():
                                        if comkey == 'items':
                                            for com in comvalue:
                                                comictemp = {}
                                                for ckey, cvalue in com.items():
                                                    if ckey == 'name':
                                                        comicslist.append(cvalue)
                                                        #comictemp['comics'] = cvalue
                                                #comicslist.append(comictemp)
                                                #characterdict['character'][comictemp]
                                else:
                                    comicslist.append('NA')
                                if 'series' in charkey:
                                    for serkey, servalue in charvalue.items():
                                        if serkey == 'items':
                                            for ser in servalue:
                                                seriestemp = {}
                                                for skey, svalue in ser.items():
                                                    if skey == 'name':
                                                        serieslist.append(svalue)
                                                   #      seriestemp['series'] = svalue
#                                                 serieslist.append(seriestemp)
                                else:
                                    serieslist.append('NA')
                                if 'events' in charkey:
                                    for evekey, evevalue in charvalue.items():
                                        if evekey == 'items':
                                            for eve in evevalue:
                                                eventstemp = {}
                                                for ekey, evalue in eve.items():
                                                    if ekey == 'name':
                                                        eventslist.append(evalue)
                                                      #   eventstemp['events'] = evalue
#                                                 eventslist.append(eventstemp)
                                else:
                                    eventslist.append('NA')
                                if 'stories' in charkey:
                                    for storkey, storvalue in charvalue.items():
                                        if storkey == 'items':
                                            for stor in storvalue:
                                                storytemp = {}
                                                for stkey, stvalue in stor.items():
                                                    if stkey == 'name':
                                                        storieslist.append(stvalue)
                                                     #    storytemp['stories'] = stvalue
#                                                     storieslist.append(storytemp)
                                                   #  else:
#                                                         storytemp['stories'] = 'NA' 
                              #           else: 
#                                             storieslist.append('NA')
                                
                                            
                                else:
                                    storieslist.append('NA')
                                    #continue
                    
                            #print characterdict

                            storieslist2.append(storieslist)
                            comicslist2.append(comicslist)
                            serieslist2.append(serieslist)
                            eventslist2.append(eventslist)
                            namelist.append(name)

#zip up lists                            
    zips = zip(namelist, comicslist2, serieslist2, eventslist2, storieslist2)
    
#Many thanks to Steven Hoeschler who pointed me to the correct way to use dictionaries and assign values to get the data structured properly
#Set/define and assign default dict
    def defaultmarvel():
        return defaultdict(defaultmarvel)
    marveldict = defaultmarvel()
#iterate through zipped list, assign name item as key to default dict, appearance items as inner keys and resulting values
    for item in zips:
        #print item[0]
        character_name = tuple(item[0])
        character_comics = tuple(item[1])
        character_series = tuple(item[2])
        character_events = tuple(item[3])
        character_stories = tuple(item[4])
        #print type(character_comics)
        marveldict[character_name]['Comics'] = character_comics
        marveldict[character_name]['Series'] = character_series
        marveldict[character_name]['Events'] = character_events
        marveldict[character_name]['Stories'] = character_stories
#iterate through each inner key of marvel default dict, write outer key and inner value to each corresponding file
    for key, value in marveldict.iteritems():
        for c in value['Comics']:
            #print type(key), type(c)
            key = str(key).decode('utf-8')
            c = c.encode('utf-8')
            key = key.replace("(u'", '').replace("',)", '')
            if c != 'NA':
                print c
                comicsfile.write(key + '\t')
                comicsfile.write(c + '\n')
                test.write(key + '\n')
        for s in value['Series']:
            key = str(key).decode('utf-8')
            s = s.encode('utf-8')
            key = key.replace("(u'", '').replace("',)", '')
            if s != 'NA':
                seriesfile.write(key + '\t')
                seriesfile.write(s + '\n')
        for e in value['Events']:
            key = str(key).decode('utf-8')
            e = e.encode('utf-8')
            key = key.replace("(u'", '').replace("',)", '')
            if e != 'NA':
                eventsfile.write(key + '\t')
                eventsfile.write(e + '\n')
        for st in value['Stories']:
            key = str(key).decode('utf-8')
            st = st.encode('utf-8')
            key = key.replace("(u'", '').replace("',)", '')
            if st != 'NA':
                storiesfile.write(key + '\t')
                storiesfile.write(st + '\n')

if __name__ == '__main__':
  main()
