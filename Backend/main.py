from database.crawler import crawl

counter = 0
for x in crawl():
    print(x)
    counter = counter + 1
    if counter == 5:
        break
