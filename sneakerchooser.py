print("Thank You For Testing My Idea")
print("This program will help you decide on which sneakers to purchase next")
print("Please answer questions exactly as they appear")
import webbrowser as wb 
height = input("Do you prefer High Top or Low Top? ")
if height == "High Top":
	print("I too need that ankle support")
elif height == "Low Top":
	print("Exposed Ankles")
else:
	print("You better not have typed mids")
print("Your preference is " + height)
brand = input("Which Brand Do You Prefer: Nike, Adidas, or New Balance? ")
if brand == "Nike":
	print("It's Lit!")
elif brand == "Adidas":
	print("Yeezy just jumped over Jumpman")
elif brand == "New Balance":
	print("I see you respect good craftsmanship")
else:
	print("Pick from one of the three")
print("Your preference is " + brand)
print("Almost there two more questions")
co = input("Do you prefer a Colorful shoe or a more Reserved look? (Type: Colorful or Reserved) ")
if co == "Colorful":
	print("Out here breaking necks")
elif co == "Reserved":
	print("Sophisticated")
else:
	print("You only have two options")
expen = input("Do you want to spend Under $100, Under $200, or No Budget? ")
if expen == "Under $100":
	print("Savvy Shopper")
elif expen == "Under $200":
	print("We can definitely work with this")
elif expen == "No Budget":
	print("Ok I see you")
else:
	print("Not sure how much you want to spend, try again")
print("Ok I can work with this")
# Everything under here is colorful under $100
if height == "High Top" and brand == "Nike" and co == "Colorful" and expen == "Under $100":
	print("You might like the Nike Blazer Mid '77 Vintage")
	wb.open("https://www.nike.com/t/blazer-mid-77-vintage-mens-shoe-nw30B2/BQ6806-111")
elif height == "Low Top" and brand == "Nike" and co == "Colorful" and expen == "Under $100":
	print("You might like the Nike Blazer Low '77 Vintage")
	wb.open("https://www.nike.com/t/blazer-low-77-vintage-mens-shoe-jsksCM/DA6364-102")
elif height == "High Top" and brand == "Adidas" and co == "Colorful" and expen == "Under $100":
	print("You might like TOP TEN RB DONOVAN MITCHELL SHOES")
	wb.open("https://www.adidas.com/us/top-ten-rb-donovan-mitchell-shoes/GW4978.html")
elif height == "Low Top" and brand == "Adidas" and co == "Colorful" and expen == "Under $100":
	print("You might like GAZELLE SHOES")
	wb.open("https://www.adidas.com/us/gazelle-shoes/BB5478.html")
elif height == "High Top" and brand == "New Balance" and co == "Colorful" and expen == "Under $100":
	print("You might like Fresh Foam Cruzv1 Reissue")	
	wb.open("https://www.newbalance.com/pd/fresh-foam-cruzv1-reissue/MCRZRV1-35865.html")
elif height == "Low Top" and brand == "New Balance" and co == "Colorful" and expen == "Under $100":
	print("You might like 574 Core")
	wb.open("https://www.newbalance.com/pd/574-core/ML574-EG.html?dwvar_ML574-EG_style=ML574EGB") 
# Everything under here is colorful under $200
elif height == "High Top" and brand == "Nike" and co == "Colorful" and expen == "Under $200":
	print("You might like Nike Air Force 1 High '07 LV8")
	wb.open("https://www.nike.com/t/air-force-1-high-07-lv8-mens-shoe-SQXJq3/CT2306-101")
elif height == "Low Top" and brand == "Nike" and co == "Colorful" and expen == "Under $200":
	print("You might like Nike Air Max 270")
	wb.open("https://www.nike.com/t/air-max-270-mens-shoe-KkLcGR/CV7544-600")
elif height == "High Top" and brand == "Adidas" and co == "Colorful" and expen == "Under $200":
	print("You might like N3XT L3V3L FUTURENATURAL SHOES")
	wb.open("https://www.adidas.com/us/n3xt-l3v3l-futurenatural-shoes/H67457.html")
elif height == "Low Top" and brand == "Adidas" and co == "Colorful" and expen == "Under $200":
	print("You might like ULTRABOOST 5.0 DNA SHOES")
	wb.open("https://www.adidas.com/us/ultraboost-5.0-dna-pride-shoes/GW5125.html")
elif height == "High Top" and brand == "New Balance" and co == "Colorful" and expen == "Under $200":
	print("You might like KAWHI")	
	wb.open("https://www.newbalance.com/pd/kawhi/BBKLSV1-36923.html")
elif height == "Low Top" and brand == "New Balance" and co == "Colorful" and expen == "Under $200":
	print("You might like Fresh Foam 880v11")
	wb.open("https://www.newbalance.com/pd/fresh-foam-880v11/M880V11-33418.html?dwvar_M880V11-33418_style=M880R11")
# Everything under here is colorful no price limit
elif height == "High Top" and brand == "Nike" and co == "Colorful" and expen == "No Budget":
	print("You might like Nike Air Yeezy 2 Red October")
	wb.open("https://stockx.com/air-yeezy-2-red-october")
elif height == "Low Top" and brand == "Nike" and co == "Colorful" and expen == "No Budget":
	print("You might like Nike Dunk SB Low Paris")
	wb.open("https://stockx.com/nike-dunk-sb-low-paris")
elif height == "High Top" and brand == "Adidas" and co == "Colorful" and expen == "No BUdget":
	print("You might like adidas NMD HU Pharrell Human Race Scarlet")
	wb.open("https://stockx.com/adidas-nmd-hu-pharrell-williams-scarlet")
elif height == "Low Top" and brand == "Adidas" and co == "Colorful" and expen == "No Budget":
	print("You might like adidas Yeezy Boost 350 V2 Glow")
	wb.open("https://stockx.com/adidas-yeezy-boost-350-v2-glow")
elif height == "High Top" and brand == "New Balance" and co == "Colorful" and expen == "No Budget":
	print("You might like New Balance 997S Bodega")	
	wb.open("https://stockx.com/new-balance-997s-bodega")
elif height == "Low Top" and brand == "New Balance" and co == "Colorful" and expen == "No Budget":
	print("You might like New Balance 1300 Ronnie Fieg Salmon Sole")
	wb.open("https://stockx.com/new-balance-1300-ronnie-fieg-salmon-sole")
# Everything Under here is reserved and under $100
elif height == "High Top" and brand == "Nike" and co == "Reserved" and expen == "Under $100":
	print("You might like the Nike Blazer Mid '77 Vintage")
	wb.open("https://www.nike.com/t/blazer-mid-77-vintage-mens-shoe-nw30B2/BQ6806-002")
elif height == "Low Top" and brand == "Nike" and co == "Reserved" and expen == "Under $100":
	print("You might like the Nike Blazer Low '77 Vintage")
	wb.open("https://www.nike.com/t/blazer-low-77-vintage-mens-shoe-jsksCM/DA6364-001")
elif height == "High Top" and brand == "Adidas" and co == "Reserved" and expen == "Under $100":
	print("You might like HOOPS 2.0 MID SHOES")
	wb.open("https://www.adidas.com/us/hoops-2.0-mid-shoes/FY8616.html")
elif height == "Low Top" and brand == "Adidas" and co == "Reserved" and expen == "Under $100":
	print("You might like SAMBA CLASSIC")
	wb.open("https://www.adidas.com/us/samba-classic/034563.html")
elif height == "High Top" and brand == "New Balance" and co == "Reserved" and expen == "Under $100":
	print("You might like New Balance 550")	
	wb.open("https://www.newbalance.com/pd/550/BB550V1-37009.html?dwvar_BB550V1-37009_style=BB550LM1")
elif height == "Low Top" and brand == "New Balance" and co == "Reserved" and expen == "Under $100":
	print("You might like 574 Core")
	wb.open("https://www.newbalance.com/pd/574-core/ML574-EG.html?dwvar_ML574-EG_style=ML574EGG")
# Everything Under here is reserved and under $200
elif height == "High Top" and brand == "Nike" and co == "Reserved" and expen == "Under $200":
	print("You might like Nike Air Force 1 '07 High")
	wb.open("https://www.nike.com/t/air-force-1-07-high-mens-shoe-XTJLXX/CT2303-100")
elif height == "Low Top" and brand == "Nike" and co == "Reserved" and expen == "Under $200":
	print("You might like Nike Air Zoom Pegasus 38")
	wb.open("https://www.nike.com/t/air-zoom-pegasus-38-mens-running-shoe-extra-wide-lq7PZZ/CW7356-002")
elif height == "High Top" and brand == "Adidas" and co == "Reserved" and expen == "Under $200":
	print("You might like FORUM MID SHOES")
	wb.open("https://www.adidas.com/us/forum-mid-shoes/FY7939.html")
elif height == "Low Top" and brand == "Adidas" and co == "Reserved" and expen == "Under $200":
	print("You might like NMD_R1 SHOES")
	wb.open("https://www.adidas.com/us/nmd_r1-shoes/G55574.html")
elif height == "High Top" and brand == "New Balance" and co == "Reserved" and expen == "Under $200":
	print("You might like New Balance 550")	
	wb.open("https://www.newbalance.com/pd/550/BB550V1-34466.html")
elif height == "Low Top" and brand == "New Balance" and co == "Reserved" and expen == "Under $200":
	print("You might like Made In US 992")
	wb.open("https://www.newbalance.com/pd/made-in-us-992/ML992V1-34303.html")
# Everything Under here is reserved with No Budget
elif height == "High Top" and brand == "Nike" and co == "Reserved" and expen == "No Budget":
	print("You might like Jordan 1 Retro High Shadow")
	wb.open("https://stockx.com/air-jordan-1-retro-high-shadow-2018")
elif height == "Low Top" and brand == "Nike" and co == "Reserved" and expen == "No Budget":
	print("You might like Nike Dunk Low Retro White Black")
	wb.open("https://stockx.com/nike-dunk-low-retro-white-black-2021")
elif height == "High Top" and brand == "Adidas" and co == "Reserved" and expen == "No Budget":
	print("You might like adidas Yeezy Boost 750 Triple Black")
	wb.open("https://stockx.com/adidas-yeezy-boost-750-triple-black")
elif height == "Low Top" and brand == "Adidas" and co == "Reserved" and expen == "No Budget":
	print("You might like adidas Yeezy Boost 350 Pirate Black")
	wb.open("https://stockx.com/adidas-yeezy-boost-350-pirate-black-2016")
elif height == "High Top" and brand == "New Balance" and co == "Reserved" and expen == "No Budget":
	print("You might like New Balance 2002R BAPE Grey")	
	wb.open("https://stockx.com/new-balance-2002r-bape-grey")
elif height == "Low Top" and brand == "New Balance" and co == "Reserved" and expen == "No Budget":
	print("You might like New Balance 992 Kith Kithmas Teal")
	wb.open("https://stockx.com/new-balance-992-kith-kithmas-teal")

print("Thanks For Playing")
