def decode(self, str->str)->List[str]:
	decode_strs= []
	while(I<len(str)):
		j = i
		while(s[j]!=‘#’): #handles_big_digits
			j+=1
		pos = int(str[I:j]) #intconversion 
		decode_strs.append(str[j+1:j+pos+1]) #appending values
		i = j+pos+1 #i update
	return decode_strs
