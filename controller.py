f=open('principals/data.tsv','r')
s=f.read().split('\n')[:20000]
f.close()
s1=[]
for i in s[1:]:
	i=list(i.split('\t'))
	j1=i[-2].split(',')
	j2=i[-1].split(',')
	s1.append("\t".join(i[:-2]+[j1[0]]+[j2[0]]))
s=s1
f1=open('principals/data1.tsv','w')
f1.write("\n".join(s))
f1.close()