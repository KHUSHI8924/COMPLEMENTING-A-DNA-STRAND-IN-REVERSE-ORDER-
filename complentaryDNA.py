t=input("Enter the nucleotide of DNA:").upper()
reverse_complement=""
for base in t:
    if base=="A":
        reverse_complement+="T"
    elif base=="C":
        reverse_complement+="G"
    elif base=="T":
        reverse_complement+="A"
    elif base=="G":
        reverse_complement+="C"
    else:
        reverse_complement+="0"
reverse_complement=reverse_complement[::-1]
print("REVERSE COMPLEMENT",reverse_complement.upper())