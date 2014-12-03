import urllib2, json, codecs
from marvel.marvel import Marvel
import time, hashlib


def main():
    
#open file to write out
    #characters = open("allcharacters.txt", "w")

#for offset in range 1402 to return all characters, decode and write out
#https://github.com/lamw/vghetto-scripts/blob/master/python/create_random_marvel_vms.py used for inspiration for timestamp and hashlib real time values   
    for i in range(1402):
        publickey = "36c31272c0df04acc5ccbaea1cbe3863"
        privatekey = "bb1367ac32167e1d090661758f17b5f76c5aa168"
        limit = '1'
        timestamp = str(int(time.time()))
        hash_value = hashlib.md5(timestamp + privatekey + publickey).hexdigest()
        url = 'http://gateway.marvel.com:80/v1/public/characters?limit=' + limit + '&offset=' + str(i) + '&apikey=' + publickey + '&ts=' + timestamp + '&hash=' + hash_value
#         url2 = "http://gateway.marvel.com/v1/comics/?apikey=%s&ts=%s&hash=%s" % (publickey, timestamp, hash_value)
        response = urllib2.urlopen(url).read()
        characterinfo = response.decode('utf-8')
        characterinfo = characterinfo.encode('utf-8')
        characters.writelines(characterinfo + '\n')

#if i did pymarvel
#     for i in range(1402):
#         m = Marvel("36c31272c0df04acc5ccbaea1cbe3863", "bb1367ac32167e1d090661758f17b5f76c5aa168")
#         character_data_wrapper = m.get_characters(limit=1, offset=i)
# #         
#         #json.dumps(character_data_wrapper, 
# #         
#         for character in character_data_wrapper.data.results:
#           #   json.dump(items, characters)
# #              print items.name, items.comics

                
                
#             json.dumps(item, characters)
      #   for item in character_data_wrapper.data.results:
#             print item.
#             print item.name, item.description, item.comics, item.stories, item.events, item.series


if __name__ == '__main__':
  main()
