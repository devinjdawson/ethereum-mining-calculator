import requests
import json
import sys
import time
r = requests.get('http://moneroblocks.info/api/get_stats/').json()
def avg(l): return sum([i for i in l])/float(len(l))
difficultyAvg = avg([int(b['difficulty']) for b in r['data']['blocks']])
r = requests.get('https://www.cryptocompare.com/api/data/price?fsym=XMR&tsyms=USD"').json()
data = {
    'blockTime': 120,
    'difficulty': 'difficulty',
    'priceUsd': 'Data.Price',
    'lastUpdate': time.time(),
}
file(sys.argv[1], 'w').write('moneroStats = ' + json.dumps(data) + ';')
