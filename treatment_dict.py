import json

treatment_dict = {
    "Velvet": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
               "https://www.amazon.com/Fritz-Aquatics-42020-Mardel-Coppersafe/dp/B00OTH68Z6/ref=sr_1_2?crid=24KHP1163TEL8&keywords=coppersafe&qid=1700420425&sprefix=coppersafe%2Caps%2C158&sr=8-2"],
    "Ich": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
             "https://www.amazon.com/Hikari-USA-Inc-Ich-Treatment/dp/B00176I3UA/ref=sr_1_4?crid=3AW66SE6Z6ENY&keywords=ich+medication&qid=1700420545&sprefix=ich+medication%2Caps%2C113&sr=8-4"],
    "Popeye": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
               "https://www.amazon.com/dp/B00CJ0VY8G?adId=B00CJ0VY8G&ref-refURL=https%3A%2F%2Fbettaboxx.webflow.io%2Fbetta-disease-illness%2Fbacterial-infection&slotNum=0&imprToken=aa2888f48105bdc5232f6face7e255ef&adType=smart&adMode=manual&adFormat=card&impressionTimestamp=1633175544164&linkCode=ll1&tag=bettaboxx-20&linkId=2d455a23214b7a5eb63f2514bfb10574&language=en_US&ref_=as_li_ss_tl&th=1"],
    "Fin Rot": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
                "https://www.amazon.com/dp/B00CJ0VY8G?adId=B00CJ0VY8G&ref-refURL=https%3A%2F%2Fbettaboxx.webflow.io%2Fbetta-disease-illness%2Fbacterial-infection&slotNum=0&imprToken=aa2888f48105bdc5232f6face7e255ef&adType=smart&adMode=manual&adFormat=card&impressionTimestamp=1633175544164&linkCode=ll1&tag=bettaboxx-20&linkId=2d455a23214b7a5eb63f2514bfb10574&language=en_US&ref_=as_li_ss_tl&th=1",
                "https://www.amazon.com/Price-Freshwater-Maracyn-Powder-Packets/dp/B001G84BWS/ref=sr_1_1?crid=1R7Q980YZU1EX&keywords=fritz+maracyn&qid=1700420817&sprefix=fritz+ma%2Caps%2C178&sr=8-1"],
    "Columnaris": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
                   "https://www.amazon.com/dp/B000HHO00C/?tag=fishlab-20",
                   "https://www.amazon.com/dp/B00CJ0VY8G?adId=B00CJ0VY8G&ref-refURL=https%3A%2F%2Fbettaboxx.webflow.io%2Fbetta-disease-illness%2Fbacterial-infection&slotNum=0&imprToken=aa2888f48105bdc5232f6face7e255ef&adType=smart&adMode=manual&adFormat=card&impressionTimestamp=1633175544164&linkCode=ll1&tag=bettaboxx-20&linkId=2d455a23214b7a5eb63f2514bfb10574&language=en_US&ref_=as_li_ss_tl&th=1"],
    "Hole in the Head": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
                         "https://www.amazon.com/Seachem-67108010-Metronidazole-5gram/dp/B0002A5X8W/ref=sr_1_2?crid=13H2H47QR4MKH&keywords=Metronidazole&qid=1700421028&s=pet-supplies&sprefix=metronidazole%2Cpets%2C283&sr=1-2"],
    "Dropsy": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
               "https://www.amazon.com/dp/B00CJ0VY8G?adId=B00CJ0VY8G&ref-refURL=https%3A%2F%2Fbettaboxx.webflow.io%2Fbetta-disease-illness%2Fbacterial-infection&slotNum=0&imprToken=aa2888f48105bdc5232f6face7e255ef&adType=smart&adMode=manual&adFormat=card&impressionTimestamp=1633175544164&linkCode=ll1&tag=bettaboxx-20&linkId=2d455a23214b7a5eb63f2514bfb10574&language=en_US&ref_=as_li_ss_tl&th=1"],
    "Swim Bladder Disorder": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
                              "https://www.amazon.com/Price-Freshwater-Maracyn-Powder-Packets/dp/B001G84BWS/ref=sr_1_3?crid=1IEG47LPKJMA4&keywords=maracyn+2&qid=1700421257&sprefix=maracyn%2Caps%2C202&sr=8-3",
                              "https://www.amazon.com/Fritz-Aquatics-ParaCleanse-Treatment-90003/dp/B09F4HV8HH/ref=sr_1_3?crid=IKADNGWFES0G&keywords=paracleanse&qid=1700421279&sprefix=paracleanse%2Caps%2C162&sr=8-3"],
    "Constipation": ["https://www.amazon.com/API-AQUARIUM-Freshwater-Aquarium-16-Ounce/dp/B000255NIC/ref=sr_1_5_pp?crid=2XVNUK58MG7JZ&keywords=aquarium+salt&qid=1700420360&sprefix=aquarium+sal%2Caps%2C220&sr=8-5",
                      "https://www.amazon.com/365-Everyday-Value-Organic-Petite/dp/B074H51Q49/ref=sr_1_2_f3_0o_wf?keywords=frozen+peas&qid=1700421303&sr=8-2"]
}

with open("treatment_links.json", "w") as outfile:
    json.dump(treatment_dict, outfile)