import urllib.request, re
urls = ['https://freeimage.host/i/qvDc3hb', 'https://freeimage.host/i/qvDay2S', 'https://freeimage.host/i/qvDcxv1']
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        m = re.search(r'property="og:image"\s+content="([^"]+)"', res)
        if m:
            print(m.group(1))
    except Exception as e:
        print('Error:', e)
