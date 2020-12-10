priceStrawberry  = float(input())
# price for all
priceRaspberry = priceStrawberry / 2
priceOrange = priceRaspberry - (priceRaspberry * 0.40)
priceBananas = priceRaspberry - (priceRaspberry * 0.80)

# quantity
qualityBananas = float(input())
qualityOrange = float(input())
qualityRaspberry = float(input())
qualityStrawberry = float(input())

needPriceS = priceStrawberry * qualityStrawberry
needPriceR = priceRaspberry * qualityRaspberry
needPriceO = priceOrange * qualityOrange
needPriceB = priceBananas * qualityBananas

allSum = needPriceS + needPriceR + needPriceO + needPriceB

print(allSum)