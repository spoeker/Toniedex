from database.crawler import crawl

# counter = 0
for x in crawl():
    print(x.title)
# counter = counter + 1
# if counter == 25:
#    break
