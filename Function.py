#This is a program to see when a certain product has been terminated, it confirms the termination year by looking in sec server and counting the percentage
#decrease. Outputs in "extra" 
#input is from "Input_Function"
#inputs are from biotech IPO cos file
from __future__ import division
import urllib
import string
import re
import requests
import itertools

OpenFile = open("C:\Python27\input_Function_.txt","a+")
lines = OpenFile.readlines()
for i in range(0,len(lines)):
	line=lines[i]
	
	id2 = line.split(",")[0].lower()
	print ("sic code",id2)
	firm_name=line.split(",")[1].strip('\t').lower()
	form_type = line.split(",")[2].strip('\t').strip().lower() 
	product_1= line.split(",")[4].strip('\t').strip('()').lower()
	product_1=product_1.strip('\t\n\r')
	
	printable = set(string.printable)
	product_1=filter(lambda x: x in printable, product_1)
	
	product_x=product_1 #this is so that it matches the right product from year to year instead of matching the shortered veersion
	print product_1
	form_year=line.split(",")[3].strip('\t')
	product_2=line.split(",")[5].strip('\t').strip('()').lower()
	
	product_2=product_2.strip('\t\n\r')
	try:
		for x in range(i+1,len(lines)):
			linea=lines[x]
			form_year_x=linea.split(",")[3].strip('\t')
			id_x=linea.split(",")[0].lower()
			if id_x!=id2:
				
				OpenFile = open("C:\Python27\input_Function_.txt","a+")
				OpenFile.write('%s%s%s' % ('\n',line.rstrip('\n'),","))
				break
			print ('checking if year is the same', linea)
			if form_year!=form_year_x and id2==id_x :
				form_year=form_year_x
				for y in range(x,x+30):
					linea_1=lines[y]
					print ('checking if product match',linea_1)
					product_y=linea_1.split(",")[4].strip('\t').strip('()').lower()
					product_y=product_y.strip('\t').lower()
					
					printable = set(string.printable)
					product_y=filter(lambda x: x in printable, product_y)
	
					product_y2=linea_1.split(",")[5].strip('\t').strip('()').lower()
					product_y2=product_y2.strip('\t').lower()
					
					printable=set(string.printable)
					product_y2=filter(lambda x: x in printable,product_y2)
					
					form_year_y=linea_1.split(",")[3].strip('\t')
					form_type_y=linea_1.split(",")[2].strip('\t').strip().lower() 
					if product_y==product_x or product_y2==product_x:
						if product_y2==product_x:
							product_x=product_y
						print ('found match', product_y,form_year,form_type_y)
						#code here should return how many matches were found in document for this year
						OpenFile2 = open(r"C:\Users\David\Desktop\ftp.txt",'r')
						lines1 = OpenFile2.readlines()
					
						for linesftp in lines1:		
							id3 = linesftp.split(",")[0].lower().strip()
							year=linesftp.split(",")[2].lower().strip()
							
							form= linesftp.split(",")[1].lower().strip()
							id4=id2[-6:]
							id1=id2[-7:]
							
							if id4==id3 or id1==id3:
							
								if form_year==year and form_type_y==form[:3] or form_year==year and form_type_y==form[:4] :
									print "found firm now going to sec server"
									#puts together the url based of the ftp server request, but it will lead to the list of documents NOT the actual document. 
									ftp = linesftp.split(",")[3].lower().strip()
									sitename=ftp[17:]
									sitename=sitename[:-4]
									sitename=sitename.replace("-","")
									backend= ftp[-25:-4]
									end="-index.htm"
									sitename="https://www.sec.gov/Archives"+sitename+backend+end
									print sitename
									d = urllib.urlopen(sitename)
									dd = d.read()
									lower_s = string.lower(dd)
									#decides if txt document avaliable or htm document
									index=lower_s.find("archives/ed")
									
									htm_index=lower_s.find(".htm",index+3,index+200)
									print ("did it find htm doc?", htm_index)
									if htm_index<1 :
										#then its text
										document_site=ftp
										print (".txt", document_site)
									else:
										
										#then its htm
										if form_type_y=="424":
											document_site=lower_s[index+8:index+65]
											document_site="https://www.sec.gov/Archives"+document_site		
											print (".htm","424", document_site)
										else:	
											ending_index=lower_s.find('">',index)
											document_site=lower_s[index+8:ending_index]
											document_site="https://www.sec.gov/Archives"+document_site		
											
										
									
									print ("final doc site", document_site)	
									#goes to the actual document
									e=urllib.urlopen(document_site)
									ee = e.read()
									lower_e = string.lower(ee)
									product_1=product_x
									product1count=lower_e.count(product_1)
									len1=len(product_1)
									while product1count<4 and len1>6:
										product_1=product_1[:-1]
										product1count=lower_e.count(product_1)
										len1=len(product_1)
									if product_2 is None:
										product2count=0
									else:
										product2count=lower_e.count(product_2)
										len2=len(product_2)
										while product2count<4 and len2>6 :	
											product_2=product_2[:-1]
											product2count=lower_e.count(product_2)
											len2=len(product_2)
										
									
					
									
					
									print (form,year,product_x,product1count)
									
									product_before=product1count
									OpenFile3= open("C:\Python27\extra.txt", 'a')
									OpenFile3.write(firm_name+","+'\t'+id2+","+"\t"+form_type_y+","+'\t'+form_year_y+","+"\t"+ product_x+","+"\t"+product_1+","+"\t"+"%d"%product1count+","+"\n")
									OpenFile3.close()
									print line

									break
									
								
							if id3=="end":
								OpenFile3= open("C:\Python27\extra.txt", 'a')
								OpenFile3.write(firm_name+","+'\t'+id2+","+"\t"+form_type_y+","+'\t'+form_year_y+","+"FTP was not found"+","+"\n")
								OpenFile3.close()
								print line
								OpenFile = open("C:\Python27\input_Function_.txt","a+")
								OpenFile.write('%s%s%s' % ('\n',line.rstrip('\n'),","))
						break
					
					
					if form_year_y!=form_year:	
						print ('product discontinued', product_x,form_year)
						
						#code here should return how many matches were found in document for this year and it should be less than above comment line
						OpenFile2 = open(r"C:\Users\David\Desktop\ftp.txt",'r')
						lines1 = OpenFile2.readlines()
					
						for linesftp in lines1:		
							id3 = linesftp.split(",")[0].strip().lower()
							year=linesftp.split(",")[2].strip().lower()
							form= linesftp.split(",")[1].strip().lower()
							id4=id2[-6:]
							id1=id2[-7:]
							if id4==id3 or id1==id3:
								if form_year==year and form_type_y==form[:3] or form_year==year and form_type_y==form[:4] :
									print "found firm now going to sec server"
									#puts together the url based of the ftp server request, but it will lead to the list of documents NOT the actual document. 
									ftp = linesftp.strip().split(",")[3].lower()
									sitename=ftp[17:]
									sitename=sitename[:-4]
									sitename=sitename.replace("-","")
									backend= ftp[-25:-4]
									end="-index.htm"
									sitename="https://www.sec.gov/Archives"+sitename+backend+end
									print sitename
									d = urllib.urlopen(sitename)
									dd = d.read()
									lower_s = string.lower(dd)
									#decides if txt document avaliable or htm document
									index=lower_s.find("archives/ed")
									
									htm_index=lower_s.find(".htm",index+3,index+200)
									print ("did it find htm doc?", htm_index)
									if htm_index<1 :
										#then its text
										document_site=ftp
										print (".txt", document_site)
									else:
										
										#then its htm
										if form_type_y=="424":
											document_site=lower_s[index+8:index+65]
											document_site="https://www.sec.gov/Archives"+document_site
											print (".htm","424", document_site)
										else:	
											ending_index=lower_s.find('">',index)
											document_site=lower_s[index+8:ending_index]
											document_site="https://www.sec.gov/Archives"+document_site
											
											
									print ("final doc site", document_site)
									#goes to the actual document
									e=urllib.urlopen(document_site)
									ee = e.read()
									lower_e = string.lower(ee)
									product_1=product_x
									product1count=lower_e.count(product_1)
									len1=len(product_1)
									while product1count<4 and len1>6:
										product_1=product_1[:-1]
										product1count=lower_e.count(product_1)
										len1=len(product_1)
									if product_2 is None:
										product2count=0
									else:
										product2count=lower_e.count(product_2)
										len2=len(product_2)
										while product2count<4 and len2>6 :	
											product_2=product_2[:-1]
											product2count=lower_e.count(product_2)
											len2=len(product_2)
									
									
									print (form,year,product_x,product1count)
									if product_before!=0:
									
										percentage_d=(product1count-product_before)/(product_before)
										print ('percentage drop', percentage_d)
									if product_before==0:
										percentage_d=0
										print('percentage drop','divide by zero')
									OpenFile3= open("C:\Python27\extra.txt", 'a')
									OpenFile3.write('discontinued this year'+","+'\t'+firm_name+","+'\t'+id2+","+'\t'+form_type_y+","+'\t'+form_year_y+","+"\t"+ product_x+","+"\t"+product_1+","+"\t"+"%d"%product1count+","+"\t"+"%.4f"%percentage_d+","+"\n")
									OpenFile3.close()	
									print line
									OpenFile = open("C:\Python27\input_Function_.txt","a+")
									OpenFile.write('%s%s%s%s%s%s' % ('\n',line.rstrip('\n'),",",form_year_y,",","%.4f"%percentage_d))
								
									break
									
									
									
						raise StopIteration
			
				
	except StopIteration: pass 
	
		
	
				