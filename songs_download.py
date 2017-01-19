import urllib,requests,bs4,re
r=requests.get('LINK TO URL FROM DOWNLOAMING WEBSITE ')
html=bs4.BeautifulSoup(r.text,"lxml")
s=html.find("table")
links=s.findAll("a")
count=0
link_128=list()
link_320=list()
for i in links:
    site = urllib.request.urlopen(i.get('href'))
    if count%2==0:
        link_128.append([i.get('href'),round((int(site.getheader('Content-Length')))/(1024**2),2)])
    else:
        link_320.append([i.get('href'), round((int(site.getheader('Content-Length'))) / (1024 ** 2), 2)])
    count += 1
names_of_songs=(s.findAll("td"))
count=0
names=list()
regex=re.compile('</strong>(.*?)<br/>')
for i in names_of_songs:
    if count%3==0:
        names.append(regex.findall(str(i)))
    count+=1
names[:] = [x for x in names if x != []]
final_name=list()
for i in names:
    final_name.append(str(i)[3:len(str(i))-2].strip())
final_name.append("All songs zip file")
final_list_128=dict();final_list_320=dict()
count=0
for i in final_name:
    final_list_128.update({i:link_128[count]})
    final_list_320.update({i:link_320[count]})
    count+=1
print('All songs with their download links and sizes \n')
for keys,values in final_list_128.items():
    print(str(keys)+': '+str(values))

