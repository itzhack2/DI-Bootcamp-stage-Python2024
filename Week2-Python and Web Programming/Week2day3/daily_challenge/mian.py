
# Challenge 1
def create_index_dictionary(word):
    index_dict = {}
    for index, letter in enumerate(word):
        if letter in index_dict:
            index_dict[letter].append(index)
        else:
            index_dict[letter] = [index]
    return index_dict

# Challenge 2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

for price in items_purchase.values():
    clean_price.strip('$')
    clean_price = clean_price.replace(',','')
    float(clean_price)
    items_purchase[item] = clean_price

print(clean_price)

# check the price
# compare/check if i have enough money for it
# put the item in he basket
# subtrack the price form my wallet
basket = []
for item,price in items_purchase.items(): #check the price
    if price <= wallet:# compare/check if i have enough money for it
        basket.append(item)# put the item in he basket
    else:
        continue
print(basket)
