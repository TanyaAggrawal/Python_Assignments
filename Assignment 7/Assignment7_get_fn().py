text = "X-DSPAM-Confidence:    0.8475";

colon = text.find('0')

get=text[colon:colon+7]

get=float(get)

print(get)
