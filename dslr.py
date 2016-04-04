#dslr command settings module
bin = '/usr/bin/gphoto2 '
capture = ' --capture-image-and-download '
filename = ' --force-overwrite --filename='
get = ' --get-config='

set = ' --set-config='

quality = '/main/capturesettings/imagequality'
basic = '=0'

fstop = '/main/capturesettings/f-number'
f3_8 = '=0'
f4 = '=1'
f4_5 = '=2'
f5 = '=3'
f5_6 = '=4'
f6_3 = '=5'
f7_1 = '=6'
f8 = '=7'
f9 = '=8'
f10 = '=9'
f11 = '=10'
f13 = '=11'
f14 = '=12'
f16 = '=13'
f18 = '=14'
f20 = '=15'
f22 = '=16'
f25 = '=17'

def getFstop(f):
        if f <= 3.8: return f3_8
        elif f <= 4: return f4
        elif f <= 4.5: return f4_5
        elif f <= 5: return f5
        elif f <= 5.6: return f5_6
        elif f <= 6.3: return f6_3
        elif f <= 7.1: return f7_1
        elif f <= 8: return f8
        elif f <= 9: return f9
        elif f <= 10: return f10
        elif f <= 11: return f11
        elif f <= 13: return f13
        elif f <= 14: return f14
        elif f <= 16: return f16
        elif f <= 18: return f18
        elif f <= 20: return f20
        elif f <= 22: return f22
        else: return f25

iso = '/main/imgsettings/iso'
iso100 = '=0'
iso200 = '=1'
iso400 = '=2'
iso800 = '=3'
iso1600 = '=4'
iso3200 = '=5'
iso6400 = '=6'
iso12800 = '=7'

def getISO(i):
	if i < 149:
		return iso100
	elif i < 300 :
		return iso200
	elif i < 600:
		return iso400
	elif i < 1200:
		return iso800
	elif i < 2400:
		return iso1600
	elif i < 4800:
		return iso3200
	elif i < 9600:
		return iso6400
	elif i <= 12800:
		return iso12800
	else:
		return iso100

shutterspeed = '/main/capturesettings/shutterspeed'
s4000 = '=0' #0.0002s
s3200 = '=1' #0.0003s
s2500 = '=2' #0.0004s
s2000 = '=3' #0.0005s
s1600 = '=4' #0.0006s
s1250 = '=5' #0.0008s
s1000 = '=6' #0.0010s
s800 = '=7' #0.0012s
s640 = '=8' #0.0015s
s500 = '=9' #0.0020s
s400 = '=10' #0.0025s
s320 = '=11' #0.0031s
s250 = '=12' #0.0040s
s200 = '=13' #0.0050s
s160 = '=14' #0.0062s
s125 = '=15' #0.0080s
s100 = '=16' #0.0100s
s80 = '=17' #0.0125s
s60 = '=18' #0.0166s
s50 = '=19' #0.0200s
s40 = '=20' #0.0250s
s30 = '=21' #0.0333s
s25 = '=22' #0.0400s
s20 = '=23' #0.0500s
s15 = '=24' #0.0666s
s13 = '=25' #0.0769s
s10 = '=26' #0.1000s
s8 = '=27' #0.1250s
s6 = '=28' #0.1666s
s5 = '=29' #0.2000s
s4 = '=30' #0.2500s
s3 = '=31' #0.3333s
s2_5 = '=32' #0.4000s
s2 = '=33' #0.5000s
s1_6 = '=34' #0.6250s
s1_3 = '=35' #0.7692s
s_1 = '=36' #1.0000s
s_1_3 = '=37' #1.3000s
s_1_6 = '=38' #1.6000s
s_2 = '=39' #2.0000s
s_2_5 = '=40' #2.5000s
s_3 = '=41' #3.0000s
s_4 = '=42' #4.0000s
s_5 = '=43' #5.0000s
s_6 = '=44' #6.0000s
s_8 = '=45' #8.0000s
s_10 = '=46' #10.0000s
s_13 = '=47' #13.0000s
s_15 = '=48' #15.0000s
s_20 = '=49' #20.0000s
s_25 = '=50' #25.0000s
s_30 = '=51' #'30'.0000s

def getShutter(s):
        if s >= 30:
                return s_30
        elif s <= 0.0002:
                return s4000
        elif s <= 0.0003:
                return s3200
        elif s <= 0.0004:
                return s2500
        elif s <= 0.0005:
                return s2000
        elif s <= 0.0006:
                return s1600
        elif s <= 0.0008:
                return s1250
        elif s <= 0.0010:
                return s1000
        elif s <= 0.0012:
                return s800
        elif s <= 0.0015:
                return s640
        elif s <= 0.0020:
                return s500
        elif s <= 0.0025:
                return s400
        elif s <= 0.0031:
                return s320
        elif s <= 0.0040:
                return s250
        elif s <= 0.0050:
                return s200
        elif s <= 0.0062:
                return s160
        elif s <= 0.0080:
                return s125
        elif s <= 0.0100:
                return s100
        elif s <= 0.0125:
                return s80
        elif s <= 0.0166:
                return s60
        elif s <= 0.0200:
                return s50
        elif s <= 0.0250:
                return s40
        elif s <= 0.0333:
                return s30
        elif s <= 0.0400:
                return s25
        elif s <= 0.0500:
                return s20
        elif s <= 0.0666:
                return s15
        elif s <= 0.0769:
                return s13
        elif s <= 0.1000:
                return s10
        elif s <= 0.1250:
                return s8
        elif s <= 0.1666:
                return s6
        elif s <= 0.2000:
                return s5
        elif s <= 0.2500:
                return s4
        elif s <= 0.3333:
                return s3
        elif s <= 0.4000:
                return s2_5
        elif s <= 0.5000:
                return s2
        elif s <= 0.6250:
                return s1_6
        elif s <= 0.7692:
                return s1_3
        elif s <= 1.0000:
                return s1
#todo add rest of shutter lookups
