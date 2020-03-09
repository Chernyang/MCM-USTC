dataset = pd.read_csv('./data/' + tsvFileName, sep='\t')
txtFile = open('./data/' + txtFileName)
for i in range(row):
    textRating = float(txtFile.readline())
    if (dataset['product_parent'][i] == product_id1):
        date = dataset['review_date'][i]
        productMonthNumber = hash(date)
        product1Rating[productMonthNumber] += dataset['star_rating'][i] * 0.8 + textRating
        product1Number[productMonthNumber] += 1
    elif (dataset['product_parent'][i] == product_id2):
        date = dataset['review_date'][i]
        productMonthNumber = hash(date)
        product2Rating[productMonthNumber] += dataset['star_rating'][i] * 0.8 + textRating
        product2Number[productMonthNumber] += 1
    elif (dataset['product_parent'][i] == product_id3):
        date = dataset['review_date'][i]
        productMonthNumber = hash(date)
        product3Rating[productMonthNumber] += dataset['star_rating'][i] * 0.8 + textRating
        product3Number[productMonthNumber] += 1

for i in range(months):
    if product1Number[i] != 0:
        average1Rating[i] = product1Rating[i] / product1Number[i]
    if product2Number[i] != 0:
        average2Rating[i] = product2Rating[i] / product2Number[i]
    if product3Number[i] != 0:
        average3Rating[i] = product3Rating[i] / product3Number[i]