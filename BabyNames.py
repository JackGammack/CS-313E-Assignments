#  File: BabyNames.py 

#  Description: Displays baby name data

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 3/20/2018

#  Date Last Modified: 3/24/2018

import urllib.request

def exists(dict, name):
    return name in dict

def rankings(dict,name):
    if( name in dict ):
        return dict[name]
    return 0

def alldecades(dict):
    alldec = []
    for key in dict:
        decades = rankings(dict,key)
        add = True
        for item in decades:
            if ( item==1001 ):
                add = False
        if( add ):
            alldec.append(key)
    return alldec

def decbyrank(dict,dec):
    byrank = []
    if( dec == 2000 ):
        dec = 10
    else:
        dec = (dec//10)%10
    for key in dict:
        decades = rankings(dict,key)
        if( decades[dec] != 1001 ):
            if( len(byrank) == 0 ):
                byrank.append(key)
            elif( len(byrank) == 1 ):
                if( decades[dec] < rankings(dict,byrank[0])[dec] ):
                    byrank.insert(0,key)
                else:
                    byrank.append(key)
            else:
                for i in range( len(byrank) ):
                    if( i == 0 and decades[dec]<rankings(dict,byrank[i])[dec] ):
                        byrank.insert(0,key)
                        break
                    elif( decades[dec]>=rankings(dict,byrank[i-1])[dec] and decades[dec]<=rankings(dict,byrank[i])[dec] ):
                        byrank.insert(i,key)
                        break
                    elif( i == len(byrank)-1 ):
                        byrank.append(key)
                        break
    
    return byrank

def getmorepop(dict):
    morepop = []
    nms = alldecades(dict)
    for item in nms:
        rnks = rankings(dict,item)
        if( sorted(rnks, reverse=True) == rnks ):
            morepop.append(item)
    return morepop

def getlesspop(dict):
    lesspop = []
    nms = alldecades(dict)
    for item in nms:
        rnks = rankings(dict,item)
        if( sorted(rnks) == rnks ):
            lesspop.append(item)
    return lesspop
            

def main():
    dict = {}
    try:
        names = urllib.request.urlopen('http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt')
        for line in names:
            line = str (line, encoding = 'utf8')
            line = line.strip()
            line = line.split()
            for i in range(1,len(line)):
                if( line[i] == '0' ):
                    line[i] = 1001
                else:
                    line[i] = int(line[i])
            dict[line[0]] = line[1:]
        names.close()
    except:
        print('File not found.')
        return
    choice = 1
    while( True ):
        print()
        print('Options:')
        print('Enter 1 to search for names.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.')
        print()
        try:
            choice = int( input('Enter choice: ') )
        except:
            choice = 7
        

        if( choice == 1 ):
            name = input('Enter a name: ')
            print()
            if ( not exists(dict,name) ):
                print(name + ' does not appear in any decade.' )
                continue
            decades = rankings(dict,name)
            low = min( decades )
            if ( low == 0 ):
                print(name + ' does not appear in any decade.')
            else:
                print('The matches with their highest ranking decade are:')
                print(name,1900 + 10*decades.index(low))

        if( choice == 2 ):
            name = input('Enter a name: ')
            decades = rankings(dict,name)
            if( decades == 0 ):
                print()
                print(name + ' does not appear in any decade.')
            else:
                st = ''
                for item in decades:
                    if( item == 1001 ):
                        st += ' ' + '0'
                    else:
                        st+=' ' + str(item)
                print()
                print(name + ':' + st)
                for i in range(len(decades)):
                    if( decades[i] == 1001 ):
                        print( str( 1900 + 10*i ) + ': 0')
                    else:
                        print( str( 1900 + 10*i ) + ': ' + str(decades[i]) )

        if( choice == 3 ):
            dec = int(input('Enter decade: '))
            print('The names are in order of rank: ')
            lst = decbyrank(dict,dec)
            if( dec == 2000 ):
                dec = 10
            else:
                dec = (dec//10)%10
            for item in lst:
                print(item + ': ' + str(dict[item][dec]) )

        if( choice == 4 ):
            nms = alldecades(dict)
            print( str(len(nms)) + ' names appear in every decade. The names are: ' )
            for item in nms:
                print(item)

        if( choice == 5 ):
            nms = getmorepop(dict)
            print( str(len(nms)) + ' names are more popular in every decade.' )
            for item in nms:
                print(item)

        if( choice == 6 ):
            nms = getlesspop(dict)
            print( str(len(nms)) + ' names are less popular in every decade.' )
            for item in nms:
                print(item)

        if( choice < 1 or choice > 6 ):
            print()
            print('Goodbye.')
            break
        

main()
        
        
        
        
