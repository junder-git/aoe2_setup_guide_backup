polefood=5000
tribute=polefood*0.7
unitrate=100/12*7
openmarketfixedbuy=100*(100-unitrate)/3
print(f"\nThe ideal food:gold is 100:{unitrate:.0f} for saracen elephant, so open market going rate for food is set by an initial sell of: {openmarketfixedbuy:.0f} food")
print(f"\nFrom poles food bank of {polefood} you could recieve tribute of: {tribute:.0f} food")
print("...OR...")
print(f"Effectively buy {tribute:.0f} tribute of food for: {tribute/100*unitrate:.0f} gold instead... so why/when to buy...\n"
      f"Food diff equation::: \nfor {polefood-tribute:.0f} food lost in {polefood} tribute "
      f"its actually worth {(polefood-tribute)/100*unitrate:.0f} "
      f"its weight in gold to the saracen..."
      f"gold gen is much faster then food gen and by feudal age saracen will be on gold gen,"
      f"with food gen so low as it is the need is there to buy that additional 1500 food")