import sys
f = open('test.txt' , mode= 'wt' , encoding='utf-8')

r = open('test.txt', mode='rt', encoding='utf-8')

f.write('coco boco soko\n')
f.write('fofofofofofofofof\n')
f.write('kdkdkdkdkdkdkd')

f.close
r.read(32)

h = open('wasteland.txt', mode='at', encoding='utf-8')
