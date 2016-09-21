#this program searches for just product na me before the IPO year for the firm. 
#inputs are from biotech ipo names
# it will look if a product will return any matches from teh clinical website (before IPO), then it will see if those matches are worth recording as data BEFORE IPO for
#firm X. It will look for company name, market matches, and therapeutic area matches. 
#output is 'new.txt'

import urllib
import string
import re
import requests
import itertools
Allergy_Immun=["immun","autoim","inflam","aller","asthm","5","allergy and immunology"]
Emergency=["acute","emergency","organ","critical","anest","9","emergency medicine"]
Antesiology=["critical","anest","migrain","pain","neuropathic","sedation","61","antesiology"]
Colon_Rectal=["intesti","prosta","bph","colon","rectal","polyps", "7","colon and rectal"]
Dermatology=["derma","skin","debrid","8","dermatology"]
Infectious_Int=["hiv","hbv", "hcv","vira","virus", "infecti","bacteria","antibiotic","23","infectious disease"]
Cardio_Int=["cardio","vascu","acute","strok","dvt","pvd","myocard","heart","cardiovas","thromb","arterial","hypertension","21","cardiology"]
Cancer_Int=["oncolo","metastatic","chemo","malignant","carcinoid","radia","prostate","tumor","stem","lymphoma","22","cancer"]
Metabolism_Endocinology_Int=["diabete","thyroid","endocri","metabo","insulin","lipid","hypothyro","hormone","24","metabolism_endocri"]
CriticalCare_Int=["organ","emergen","critical","trauma","injur","25","critical care"]
Gastronology_Int=["gastro","liver","ulcer","intestin","stomach","abdomina","bowel","26","gastronology"]
Hematology_Int=["blood","hematol","anemia","anemic","sickle","hemophil","leukemia","lymphoma","27","hematology"]
Nephrology_Int=["renal","kidney","urinary","28","nephrology"]
Pulmonary_Int=["pulmonar","lung","asthma","cardiopulm","respira","bronchitis","asthma","pneumonia","respira","29","pulmonary"]
Rheumatology_Int=["arthritis","joint","muscle","ligament","rheumat","musculoskeletal","20","rheumatology"]
Genetics=["heredita","genetic","gene","30","genetic"]
Neurology=["neurol","nervous","neuropathic","brain","psychi","cognitive","addict","central nervous","cns","stroke","parkinson","alzheimer","40","neuro"]
Nuclear_Medicine=["nuclear","radioactive","radio","tracers","50","nuclear_medicine","50","nuclear_medicine"]
Radiology=["radiopharm","imaging","radiology","ultrasound","electromagnetic","60","radiology"]
obstetrics_gynecology=["gyneco","obstet","reprodu","female","labor","pelvic","female","infertili","vagin","70","obstetrics_gynecology"]
opthamalogy=["ophthal","glaucoma","eye","retina","macular","vision","1","opthamalogy"]
otolaryngology=["head","neck","ear","heari","sinus","reconstructive","2","Otolaryngology"]
urulogy=["urinary","urolog","bladder","incontinence","pelvic","3","urology"]
sleep_subspec=["sleep","insomnia","63","sleep_subspec"]


Main=[Allergy_Immun,Emergency,Antesiology,Colon_Rectal,Dermatology,Infectious_Int,Cardio_Int,Cancer_Int,Metabolism_Endocinology_Int,CriticalCare_Int,Hematology_Int,Nephrology_Int,Pulmonary_Int,Rheumatology_Int,Neurology,Genetics,Nuclear_Medicine,Radiology,obstetrics_gynecology,opthamalogy,otolaryngology,urulogy,sleep_subspec]




OpenFile = open(r"C:\Python27\new.txt","r")
lines = OpenFile.readlines()
List=["40","39","38","37","36","35","34","33","32","31","30","29","28""27","26","25","24","23","22","21","20","19","18","17","16","15","14","13","12","11","10","9","8","7","6","5","4","3","2","1"]
Outfile1= open("C:\\Python27\\new.txt", 'a')
op=1
for line in lines:
	if op==1:
		id2 = line.split(",")[0].strip('\t').lower()
		power=id2	#so that the file path only has the original company name and not several shortned versions of the company name
		print id2
		search=1
		syntax=1
		firm_name=line.split(",")[1].strip('\t').lower()
		form_type = line.split(",")[2].strip('\t').strip().lower() 
		print form_type
		product_1= line.split(",")[5].strip('\t').lower()
		print product_1	
		form_year=line.split(",")[3].strip('\t')
		print form_year
		therapeutic=line.split(",")[6].strip('\t').lower()
		form_year1=line.split(",")[4].strip("\t")
		market_number=line.split(",")[7].strip('\t')
		market_number1=line.split(",")[8].strip('\t')
		market_number2=line.split(",")[9].strip('\t')
		
		drug1=product_1
		p=0
		for i in drug1:											#Cleans the product names from unwante charetevers 
			if ord(i)>128 :
				drug1=drug1.replace(i,"").strip(i).strip()	
				
		x=len(drug1)		
		
		while search>0 and x>5 or syntax>0 and x>5 :	#searches for drug until the length is to short
			print ("Drug name searched for",drug1)
			print form_year
			website = 'https://clinicaltrials.gov/ct2/results?'
			data={"term":"","recr":"","rslt":"","type":"","cond":"","intr":drug1,"titles":"","outc":"","spons":"","lead":"","id":"","state1":"","cntry1":"","state2":"","cntry2":"","state3":"","cntry3":"","locn":"","gndr":"","rcv_s":"","rcv_e":"12/30/"+form_year,"lup_s":"","lup_e":""}
			r = requests.get(website, params=data,verify=False)
			print(r.url)
			filepath="C:\Users\David\Desktop"+ power+"_"+form_year+"_"+"clinicaltrials"
			print filepath
			f=open(filepath,"w") 
			f.write(r.content)
			f.close()	
			r=open(filepath, "r")
			s=r.read()
			x=len(drug1)															
			search=s.find("no studies found")			#looks for 0 studies
			syntax=s.find("syntax")
			print search
			print syntax
			if search==-1 and syntax==-1 :											#if it found result (s)
				print "print found a match"
				
				
				beg=s.find("results-summary")
				end=s.find("studies found for")				#how many studies have been found?
				if end==-1 :
					end=s.find("study found for")
				for num in List:
					number=s.find(num,beg,end)
					if number>0:
						website = 'https://clinicaltrials.gov/ct2/results?'
						data={"term":"","recr":"","rslt":"","type":"","cond":"","intr":drug1,"titles":"","outc":"","spons":"","lead":"","id":"","state1":"","cntry1":"","state2":"","cntry2":"","state3":"","cntry3":"","locn":"","gndr":"","rcv_s":"","rcv_e":"12/30/"+form_year,"lup_s":"","lup_e":""}
						rr= requests.get(website, params=data,verify=False)
						path="C:\Users\David\Desktop"+ "clinicaltrialstest"+"_"+"sample"+"_"+"clinicaltrials"
						ff=open(path,"w") 
						ff.write(rr.content)
						ff.close()
						rr=open(path, "r")
						ss=rr.read()
						xx=0
						index1=0
						index=0
						while index !=-1:
							weight1=0
							weight2=0
							weight3=0
							weight4=0
							weight5=0
							weight6=0
							weight7=0
							weight8=0
							weight9=0
							weight10=0
							weight11=0
							weight12=0
							phase=0
							study_year=0
							index=ss.find("Show study",index1)		#looks for the NC code in order to ask for it and get the full lab report
							print ('index found', index)
							code=ss[index+11:index+22]
							print code
							site='https://clinicaltrials.gov/ct2/show/'+code+ '?'
							data1={"term":"","recr":"","rslt":"","type":"","cond":"","intr":drug1,"titles":"","outc":"","spons":"","lead":"","id":"","state1":"","cntry1":"","state2":"","cntry2":"","state3":"","cntry3":"","locn":"","gndr":"","rcv_s":"","rcv_e":"12/30/"+form_year,"lup_s":"","lup_e":""}
							cc=requests.get(site,params=data1,verify=False)
							print (cc.url)
							path1="C:\Users\David\Desktop"+ power+"_"+"actuallabreport"+"_"+"clinicaltrials"
							fff=open(path1,"w")
							fff.write(cc.content)
							fff.close()
							rrr=open(path1,"r")
							fff=rrr.read()
							sss=string.lower(fff)
							#looks for phase
							phase_index=sss.rfind('<td class="body3" nowrap>')
							print ("phase index", phase_index)
							phase=sss[phase_index+26:phase_index+50]
							phase=phase.strip().strip("\t")
							
							test=phase
							while test!="phase" and len(test)>2:
								test=test[:-1]
								
							if test=="phase"	:
								print ("found phase",phase)
							else:
								phase=0
							#looks for study year
							study_year_index=sss.find('first received: <span class=')
							study_year_final=sss.find('</span',study_year_index+30)
							
							
							print ('study year index' ,study_year_index)
							study_year=sss[study_year_index+38:study_year_final]
							print ('study year',study_year)
							if study_year_index==-1:
								study_year=0
								
							#looks for the therapeutic area in the study		
							thera=sss.count(therapeutic)
							thera_1=therapeutic
							thera_length=len(thera_1)
							while thera==0 and thera_length>4:
								thera_1=thera_1[-(thera_length-1):]
								thera_length=len(thera_1)
								thera=sss.count(thera_1)
								
							thera2=sss.count(therapeutic)	
							thera_2=therapeutic	
							thera_length=len(thera_2)
							while thera2==0 and thera_length>4:
								thera_2=thera_2[:thera_length-1]
								thera_length=len(thera_2)
								thera2=sss.count(thera_2)
							if thera2 >=1 or thera>=1 :
								weight12=12
								#weight 12 means it found the therapeutic area listed in excel on the clinical study lab report.
								
							#starts looking for the firm name
							firm_index=sss.find("sponsor")						
							firm_index1=sss.find("information provided by")
							firm=sss.find(firm_name,firm_index,firm_index1)
							firmlength=6
							while firm<0 and firmlength>5 : 
								firm_name=firm_name[:firmlength-1]
								firmlength=len(firm_name)
								firm=sss.find(firm_name,firm_index,firm_index1)
							if firm >0 and weight1!=1:
								weight1=1  #first weight labeled due to firm name 
								print ("found firm name in sponsor",firm)
								#gathers the collaborator and sponsor information but doesn't look for it in the sec files just yet. 
							if firm <0 :
								collab_exist=sss.find('collaborator:</div>')
								if collab_exist>0 :
									collab_sponsor_index=sss.find('sponsors and collaborators')
									collab_sponsor_index1=collab_sponsor_index+82
									sponsor_end_index=sss.find('</div>',collab_sponsor_index1+8)
									sponsor=sss[collab_sponsor_index1:sponsor_end_index]
									print ('sponsor',sponsor)
								
									collaborator_index=sss.find('<div class="info-text">',collab_exist+5)
									collaborator_index1=sss.find('</div>',collaborator_index+8)
									collaborator=sss[collaborator_index+23:collaborator_index1]
									collaborator=collaborator.strip().strip("\t")
									print('collaborator',collaborator)
								if collab_exist==-1:
									collab_sponsor_index=sss.find('sponsors and collaborators')
									collab_sponsor_index1=collab_sponsor_index+82
									sponsor_end_index=sss.find('</div>',collab_sponsor_index1+8)
									sponsor=sss[collab_sponsor_index1:sponsor_end_index]
									print ('sponsor',sponsor)
									
									collaborator=None
							#starts looking for the drug in the intervention.Usually though the drug is scentific. Look for that chemical name in the sec documents. If nothing found than move on to below	
							interindex=	sss.find("condition, intervention")
							interindex1=sss.find("study type")
							drug1=drug1.strip()
							interindex2=sss.find(drug1,interindex,interindex1)
							#looks to see if the product name from biotecch is in the intervention section of clinical trials
							if interindex2>0  :		
								weight2=2  #second label for product name found in intervention section 
								print ("found drug in intervention", weight2)

							for item in Main:
								print item
								totalcount=0
								Lista=item
								for position in Lista:
									if position.isdigit()==False:
										marketcount=sss.count(position)
										totalcount=marketcount+totalcount
								print (totalcount,Lista[-1])
								if totalcount>3 and Lista[-2]==market_number or totalcount>3 and Lista[-2]==market_number1 or totalcount>3 and Lista[-2]==market_number2 :
									print ("the following market matches", Lista[-1])
									weight3=3 #third label due to market that was found all over the lab
									
								if totalcount>3 and weight3!=3:
									print ("clinical study different market than market of our firm")
									if totalcount>20:
										if interindex2<=0:
											weight4=4 #label due to market found but not that was listed on the excel sheet for that drug 
										
							chemindex=sss.find("hit_syn")
							if chemindex>0 or firm<0: 						#here its done looking if the drug is found in intervention, and now checks the chemical name in sec.gov/sponsor name in sec.gov
								
								print ("if this is printing it will now look for chemical name")
								intervention=sss[chemindex+9:chemindex+20]		
								print ("this is the chemical name", intervention)					
								intercount=0
								interlength=len(intervention)

								OpenFile2 = open(r"C:\Users\David\Desktop\ftp.txt",'r')
								lines1 = OpenFile2.readlines()
								for linesftp in lines1:
									print "now moved to the next line in ftp"
									
									id3 = linesftp.split(",")[0].lower().strip()
									year=linesftp.split(",")[2].lower().strip()
									form= linesftp.split(",")[1].lower().strip()
									id4=id2[-6:]
									id1=id2[-7:]
									print ("sic number:",id1,id2,id3)		
									if id4==id3 or id1==id3:
										print "found firm in ftp and now going to sec server"
										print form 
										
										sitename = linesftp.split(",")[3].strip().lower()
										print sitename
										d = urllib.urlopen(sitename)
											
										secc=d.read()
											
										secc = string.lower(secc)	
										intercount=secc.count(intervention)
										sponsorcount=secc.count(sponsor)
										sponsorcount_1=sponsorcount	
										sponsorlength=len(sponsor)
										sponsor=sponsor.strip()
										print ('this is the sponsor its looking for in sec',sponsor,sponsorcount,sponsorlength)
										words=0
										words1=0
										words2=0
										words3=0
										words4=0
										words5=0
										words6=0
										words_1=0
										words_2=0
										words_3=0
										words_4=0
										words_5=0
										words_6=0
										words__0=0
										words__1=0
										words__2=0
										words__3=0
										words__4=0
										words__5=0
										words__6=0
										rwords=0
										rwords1=0
										rwords2=0
										rwords3=0
										rwords4=0
										rwords5=0
										rwords6=0
										rwords_0=0
										rwords_1=0
										rwords_2=0
										rwords_3=0
										rwords_4=0
										rwords_5=0
										rwords_6=0
										
	
										if collab_exist!=-1:
											collaboratorlength=len(collaborator)
											collaboratorcount=secc.count(collaborator)
											print ('this is the collaborator its looking for in sec',collaborator,collaboratorcount,collaboratorlength)
										while sponsorcount_1==0 and sponsorlength>5 and sponsorlength<100 and weight1==0 	:					#searches for the sponsor found in clinical trials (of course if the firm name already found in clinical then doesnt do this if statement) and sees if it is mentioned in the sec.gov S-1
											print ('this is one interation')
											sponsor=sponsor.strip()
											sponsor_1=sponsor[:sponsorlength-1]
											sponsorlength=len(sponsor_1)
											sponsorcount_1=secc.count(sponsor_1)
											print ('searching for sponsor....', sponsor_1)
										print ("sponsorcount:", sponsorcount_1)	
										if sponsorcount==1 :	
											sponsorindex=secc.find(sponsor)												#determines what role the sponsor plays according to the sec file
											words=secc.count("collaborat",sponsorindex-100,sponsorindex+100)
											words1=secc.count("ph.d",sponsorindex-100,sponsorindex+100)
											words2=secc.count("president",sponsorindex-100,sponsorindex+100)
											words3=secc.count("director",sponsorindex-100,sponsorindex+100)
											words4=secc.count("university",sponsorindex-100,sponsorindex+100)
											words5=	secc.count("compet",sponsorindex-100,sponsorindex+100)
											words6=secc.count("obsolete",sponsorindex-100,sponsorindex+100)
											print ("found sponsor only once in sec")
											if words> 2 :
												print ("found sponsor in sec as a collaborator",sponsor)
												weight5=5
											if words1+words2+words3+words4>2:
												weight6=6
												print ("found sponsor in sec as a background for director", sponsor)
													
													
											if words5+words6>2: 
												print ("found sponsor as competitor",sponsor)
												weight7=7
													
										if sponsorcount>1:
											sponsorindex=secc.find(sponsor)
											print ('index where sponsor was found',sponsorindex)
											if sponsorindex>1:
												print 'found sponsor somwhere'	
												words=secc.count("collaborat",sponsorindex-100,sponsorindex+100)
												words1=secc.count("ph.d",sponsorindex-100,sponsorindex+100)
												words2=secc.count("president",sponsorindex-100,sponsorindex+100)
												words3=secc.count("director",sponsorindex-100,sponsorindex+100)
												words4=secc.count("university",sponsorindex-100,sponsorindex+100)
												words5=	secc.count("compet",sponsorindex-100,sponsorindex+100)
												words6=secc.count("obsolete",sponsorindex-100,sponsorindex+100)
													
											sponsorindex_1=secc.find(sponsor,sponsorindex+20)
											if sponsorindex_1>1 :
												print 'found sponsor somwhere'	
												words_0=secc.count("collaborat",sponsorindex_1-100,sponsorindex_1+100)
												words_1=secc.count("ph.d",sponsorindex-100,sponsorindex+100)
												words_2=secc.count("president",sponsorindex-100,sponsorindex+100)
												words_3=secc.count("director",sponsorindex-100,sponsorindex+100)
												words_4=secc.count("university",sponsorindex-100,sponsorindex+100)
												words_5=secc.count("compet",sponsorindex-100,sponsorindex+100)
												words_6=secc.count("obsolete",sponsorindex-100,sponsorindex+100)
													
											sponsorindex_2=secc.find(sponsor, sponsorindex_1+20)
											if sponsorindex_2>1	:
												print 'found sponsor somwhere'
												words__0=secc.count("collaborat",sponsorindex_2-100, sponsorindex_2+100)
												words__1=secc.count("ph.d",sponsorindex_2-100, sponsorindex_2+100)
												words__2=secc.count("president",sponsorindex_2-100, sponsorindex_2+100)
												words__3=secc.count("director",sponsorindex_2-100, sponsorindex_2+100)
												words__4=secc.count("university",sponsorindex_2-100, sponsorindex_2+100)
												words__5=secc.count("compet",sponsorindex_2-100, sponsorindex_2+100)
												words__6=secc.count("obsolete",sponsorindex_2-100, sponsorindex_2+100)
													
											sponsorindex_3=secc.rfind(sponsor)
											if sponsorindex_3>1:
												print 'found sponsor somwhere'
												rwords=secc.count("collaborat",sponsorindex_3-100, sponsorindex_3+100)
												rwords1=secc.count("ph.d",sponsorindex_3-100,sponsorindex_3+100)
												rwords2=secc.count("president",sponsorindex_3-100,sponsorindex_3+100)
												rwords3=secc.count("director",sponsorindex_3-100,sponsorindex_3+100)
												rwords4=secc.count("university",sponsorindex_3-100,sponsorindex_3+100)
												rwords5=secc.count("compet",sponsorindex_3-100,sponsorindex_3+100)
												rwords6=secc.count("obsolete",sponsorindex_3-100,sponsorindex_3+100)
												
											sponsorindex_4=secc.rfind(sponsor,sponsorindex_3-20)
											if sponsorindex_4>1 :
												print 'found sponsor somwhere'
												rwords_0=secc.count("collaborat",sponsorindex_4-100,sponsorindex_4+100)
												rwords_1=secc.count("pd.d",sponsorindex_4-100,sponsorindex_4+100)
												rwords_2=secc.count("president",sponsorindex_4-100,sponsorindex_4+100)
												rwords_3=secc.count("director",sponsorindex_4-100,sponsorindex_4+100)
												rwords_4=secc.count("university",sponsorindex_4-100,sponsorindex_4+100)
												rwords_5=secc.count("compet",sponsorindex_4-100,sponsorindex_4+100)
												rwords_6=secc.count("obsolete",sponsorindex_4-100,sponsorindex_4+100)
											collaboratorvariable= words+words_0+words__0+rwords+rwords_0
											print ("collaboratorvariable", collaboratorvariable )
											directorvariable=words1+words2+words3+words4+words_1+words_2+words_3+words_4+words__1+words__2+words__3+words__4+rwords1+rwords2+rwords3+rwords4+rwords_1+rwords_2+rwords_3+rwords_4	
											print ("directorvariable", directorvariable)
											competitorvariable=words5+words6+words_5+words_6+words__5+words__6+rwords5+rwords6+rwords_5+rwords_6
											print ("competitorvariable", competitorvariable)
											if collaboratorvariable>2:
												print("sponsor from clinical trial is collaborator in sec")
												weight5=5
											if directorvariable>2:
												print ("sponsor from clinical trial is background for director in sec")
												weight6=6
											if competitorvariable>2:
												print("sponsor from clinical trial is compeitor in sec")
												weight7=7
											
								
										if collab_exist!=-1:	
											while collaboratorcount==0 and collaboratorlength>6 and weight1!=1 and collaboratorlength<50:		#searches for collaborator listed in clinical trials in the sec file
												collaborator=collaborator.strip()
												collaborator=collaborator[:collaboratorlength-1]
												collaboratorlength=len(collaborator)
												collaboratorcount=secc.count(collaborator)	
												print ('searching for collaborator....',collaborator)
											if collaboratorcount==1: 
												collaboratorindex_1=secc.find(collaborator)
												words=secc.count("collaborat",collaboratorindex_1-100,collaboratorindex_1+100)
												words1=secc.count("ph.d",collaboratorindex_1-100,collaboratorindex_1+100)
												words2=secc.count("president",collaboratorindex_1-100,collaboratorindex_1+100)
												words3=secc.count("director",collaboratorindex_1-100,collaboratorindex_1+100)
												words4=secc.count("university",collaboratorindex_1-100,collaboratorindex_1+100)
												words5=secc.count("compet",collaboratorindex_1-100,collaboratorindex_1+100)
												words6=secc.count("obsolete",collaboratorindex_1-100,collaboratorindex_1+100)
												print ("found collaborator only once in sec")
												if words> 2 :
													print ("found collaborator in sec as a collaborator",collaborator)
													weight8=8
												if words1+words2+words3+words4> 2:
													print ("found collaborator in sec as a background for director", collaborator)
													weight9=9
												if words5+words6>2 : 
													print ("found collaborator as competitor",collaborator)
													weight10=10
												
												
												
											if collaboratorcount>1	:
												collaboratorindex=secc.find(collaborator)
												if collaboratorindex>1 :
													words=secc.count("collaborat",collaboratorindex-100,collaboratorindex+100)
													words1=secc.count("ph.d",collaboratorindex-100,collaboratorindex+100)
													words2=secc.count("president",collaboratorindex-100,collaboratorindex+100)
													words3=secc.count("director",collaboratorindex-100,collaboratorindex+100)
													words4=secc.count("university",collaboratorindex-100,collaboratorindex+100)
													words5=secc.count("compet",collaboratorindex-100,collaboratorindex+100)
													words6=secc.count("obsolete",collaboratorindex-100,collaboratorindex+100)
														
												collaboratorindex_1=secc.find(collaborator,collaboratorindex+20)													
												if collaboratorindex_1>1 :
													words_0=secc.count("collaborat",collaboratorindex_1-100,collaboratorindex_1+100)
													words_1=secc.count("ph.d",collaboratorindex_1-100,collaboratorindex_1+100)	
													words_2=secc.count("president",collaboratorindex_1-100,collaboratorindex_1+100)	
													words_3=secc.count("director",collaboratorindex_1-100,collaboratorindex_1+100)
													words_4=secc.count("university",collaboratorindex_1-100,collaboratorindex_1+100)
													words_5=secc.count("compet",collaboratorindex_1-100,collaboratorindex_1+100)
													words_6=secc.count("obsolete",collaboratorindex_1-100,collaboratorindex_1+100)
													
												collaboratorindex_2=secc.find(collaborator, collaboratorindex_1+20)
												if collaboratorindex_2>1:
													words__0=secc.count("collaborat",collaboratorindex_2-100,collaboratorindex_2+100)
													words__1=secc.count("ph.d",collaboratorindex_2-100,collaboratorindex_2+100)
													words__2=secc.count("president",collaboratorindex_2-100,collaboratorindex_2+100)
													words__3=secc.count("director",collaboratorindex_2-100,collaboratorindex_2+100)
													words__4=secc.count("university",collaboratorindex_2-100,collaboratorindex_2+100)
													words__5=secc.count("compet",collaboratorindex_2-100,collaboratorindex_2+100)
													words__6=secc.count("obsolete",collaboratorindex_2-100,collaboratorindex_2+100)
													
												collaboratorindex_3=secc.rfind(collaborator)			
												if collaboratorindex_3>1:
													rwords=secc.count("collaborat",collaboratorindex_3-100, collaboratorindex_3+100)
													rwords1=secc.count("ph.d",collaboratorindex_3-100, collaboratorindex_3+100)
													rwords2=secc.count("president",collaboratorindex_3-100, collaboratorindex_3+100)
													rwords3=secc.count("director",collaboratorindex_3-100, collaboratorindex_3+100)
													rwords4=secc.count("university",collaboratorindex_3-100, collaboratorindex_3+100)
													rwords5=secc.count("compet",collaboratorindex_3-100, collaboratorindex_3+100)
													rwords6=secc.count("obsolete",collaboratorindex_3-100, collaboratorindex_3+100)
															
												collaboratorindex_4=secc.rfind(collaborator, collaboratorindex_3-20)		
												if collaboratorindex_4>1:		
													rwords_0=secc.count("collaborat",collaboratorindex_4-100, collaboratorindex_4+100)
													rwords_1=secc.count("ph.d",collaboratorindex_4-100, collaboratorindex_4+100)	
													rwords_2=secc.count("president",collaboratorindex_4-100, collaboratorindex_4+100)
													rwords_3=secc.count("director",collaboratorindex_4-100, collaboratorindex_4+100)
													rwords_4=secc.count("university",collaboratorindex_4-100, collaboratorindex_4+100)
													rwords_5=secc.count("compet",collaboratorindex_4-100, collaboratorindex_4+100)
													rwords_6=secc.count("obsolete",collaboratorindex_4-100, collaboratorindex_4+100)
												collaboratorvariable= words+words_0+words__0+rwords+rwords_0
												directorvariable=words1+words2+words3+words4+words_1+words_2+words_3+words_4+words__1+words__2+words__3+words__4+rwords1+rwords2+rwords3+rwords4+rwords_1+rwords_2+rwords_3+rwords_4	
												competitorvariable=words5+words6+words_5+words_6+words__5+words__6+rwords5+rwords6+rwords_5+rwords_6
												if collaboratorvariable>2:
													print("collaborator from clinical trial is collaborator in sec")
													weight8=8
												if directorvariable>2:
													print ("collaborator from clinical trial is background for director in sec")
													weight9=9
												if competitorvariable>2:
													print("collaborator from clinical trial is compeitor in sec")
													weight10=10
												if sponsorcount==0:
													print ("found no sponsor in sec", sponsor)

														
											

										if collaborator==0 :
											print("found no collaborator in sec")
												
											
											
											
											
										while intercount<=1 and interlength>5: 			#counts how many times the chemical name is mentioned if at all in the sec.fov S-1
											intervention=intervention[:interlength-1]
											interlength=len(intervention)
											intercount=secc.count(intervention)
											print ("still looking for chemical name",intervention)
										if intercount>1 :
											print ("found chemical name in sec", intercount,intervention)
											weight11=11
												
												
										
										DeleteList=[words,words1,words2,words3,words4,words5,words6,words_1,words_2,words_3,words_4,words_5,words_6,words__0,words__1,words__2,words__3,words__4,words__5,words__6,rwords,rwords1,rwords2,rwords3,rwords4,rwords5,rwords6,rwords_0,rwords_1,rwords_2,rwords_3,rwords_4,rwords_5,rwords_6]
										
										
										 
										
										
							
									
							print "ran through all of ftp lines"
							print (cc.url)
							index1=index+15
							xx=xx+1
						
						
							Range=[weight1,weight2,weight3,weight4,weight5,weight6,weight7,weight8,weight9,weight10,weight11,weight12,phase,study_year]
							david= itertools.ifilter(lambda x: x>0,Range)
							torres=list(david)
						
							OpenFile= open("C:\\Python27\\new.txt", 'a')
							OpenFile.write('%s%s%s%s%s%s%s%s%s%s' % ('\n',line.rstrip('\n'),",",drug1,",",torres,",",sponsor,",",collaborator))
							print(beg,number,end, num)
							print "wrote on the new file, should be looking for next drug"
					
				
			drug1=drug1[:x-1]	
			x=len(drug1)
				
			
OpenFile.close()	