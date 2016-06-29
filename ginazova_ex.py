import re

def rfile (name):
    f = open (name, 'r', encoding = 'utf-8')
    fr = f.read()
    f.close()
    return fr

def snames(fr):
    regex = re.findall ('[А-Я]\.+\s?[А-Я][а-я]+', fr)
    for m in regex:
        print (m)
        
def allnames(fr):
    regex1 = re.findall ('[А-Я]\.+\s?[А-Я]\.+\s?[А-Я][а-я]+', fr)
    regex2 = re.findall('[А-Я][а-я]+\s+[А-Я][а-я]+', fr)
    for i in regex1:
        print(i)
    for l in regex2:
        print(l)
    
def main():
    snames(rfile('m.txt'))
    allnames(rfile('m.txt'))


if __name__ == '__main__':
    main()
