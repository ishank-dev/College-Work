class Reverse:
	def __init__(self,sentence):
		self.sentence = sentence
    
	def reverse(self):
		reverseSen = ' '.join(reversed(self.sentence.split()))
		# print(reverseSen,'\n\n')
		return reverseSen
    
	def vowelCount(self):
		count = 0
		vowels = ['a','e','i','o','u']
		for i in self.sentence.lower():
			if i in vowels:
				count += 1
		return count
    
# REMEMBER TO TAKE STRING WITH DIFFERENT VOWEL COUNT otherwise dictionary will not be able to hold the duplicates

r1 = Reverse(input("Enter a string"))
r2 = Reverse(input("Enter another string"))
r3 = Reverse(input("Enter the third one"))

c1 = r1.vowelCount()
c2 = r2.vowelCount()
c3 = r3.vowelCount()

wordsDesc = {
    c1:r1.reverse(),
    c2:r2.reverse(),
    c3:r3.reverse()
}

for i in sorted(wordsDesc.keys(),reverse=True):
    print(i,wordsDesc[i])