from database.crawler import crawl

counter = 0
for x in crawl():
    print(x.image)
    break
