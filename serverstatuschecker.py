#Youtube : Py
#Coded By Shin Code
#My Friend : Jenderal92 - h0d3_g4n - Moslem - Kiddenta - Naskleng45

import requests,re,random,sys,time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
               SERVER STATUS CHECKER | Python Code
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)
Banner()

def ssc(url):
	try:
		users = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Referer': 'https://tools.webconfs.com/en/server-status-checker/output',
		'Cookie': 'PHPSESSID=6b136ed37ed9dec73d8043457a408eb0; _ga=GA1.2.2073532857.1640347693; _gid=GA1.2.291062193.1640347693'}
		datas = {'data' : url,
		'submit' : 'Submit'}
		urll = requests.post("https://tools.webconfs.com/en/server-status-checker/output",data=datas, headers=users)
		if 'HTTP Code' in urll.content:
			a = re.findall('<td>(.*?)</td>' ,urll.content)
			print(url +' : '+ a[7] +' '+ 'Status : ' + a[9])
			open('A.txt', 'a').write(url +': '+ a[7] +' '+ 'Status : ' + a[9]+'\n')
		else:
			print('Coded By Shin_Code')
	except: pass


url_list = raw_input("URL LIST : ")
urr = open(url_list, 'r').readlines()
def main():
	for i in urr:
		try:
			site = i.strip()
			data=ssc(site)
		except:
			pass

pool = ThreadPool(7)
pool.map(ssc, urr)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success")