import pandas as pd
import matplotlib.pyplot as plt
import os


def Pareto_analysis(df,title):
    df = df.sort_values(by='Count',ascending=False)
    df["cumpercentage"] = df["Count"].cumsum()/df["Count"].sum()*100
    fig, ax = plt.subplots()
    ax.bar(df.index, df["Count"], color='yellow')
    ax2 = ax.twinx()
    ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
    ax.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")
    ax.set_xticklabels(df.index,fontsize=10, fontweight='bold', rotation=45, color='darkblue')
    ax.set_title(title,fontsize=15, fontweight='bold')
    for i in ax.patches:
        ax.text(i.get_x()+0.25,i.get_width()+10,str(round(i.get_height(),2)),fontsize=11, fontweight='bold',color='black')
    fig = plt.gcf()
    fig.set_size_inches(10,5)
    plt.show()

	# Change directory 
#os.chdir("C:\SS 2018\Initiatives")
df_input =pd.read_csv('Defects Log.csv', encoding='cp1252')
df_input.columns

	#Before Analysis

def_count_type=df_input['Defect Type']
def_count_type= pd.DataFrame(data=def_count_type)
def_count_type.insert(loc=1,column='Count', value=1)
out_def=def_count_type.groupby('Defect Type').count()
out_def1 = out_def[out_def['Count'] > 20]
Before_analysis=out_def1.sort_values(['Count'])
	
	#After Analysis

def_type_analysis=df_input[['Defect Type','R&D Comments']]
def_type_analysis= pd.DataFrame(data=def_type_analysis)
def_type_analysis.insert(loc=1,column='Count', value=1)
	

#pattern = ['Amended','Updated','SRN','Code Deployed','promoted','code deployed','changed','amended','updated']
pattern = ['Change','Amended','Updated','SRN','Code Deployed','promoted']
pattern_ex=['PCR','CR','design','requirement']


	#Check if any pattern is found in 'R&D Comments'  and its not due to PCR or Design


for i in range(len(def_type_analysis)):
	if any(word in str(def_type_analysis['R&D Comments'][i]) for word in pattern):
		# Exclude the defect type where change is due to ADD, CR, Requirements
		if any(word in str(def_type_analysis['R&D Comments'][i]) for word in pattern_ex):
			print ("Changes due to CR/ADD/Req-Not a defect- Item#",i)
		else:               
		# check and change 'Defect Type' to 'Code'
			
			if "Code" not in def_type_analysis['Defect Type'][i]:
				print ("Defect type changed- Item#",i,def_type_analysis['Defect Type'][i])
				def_type_analysis.loc[i,'Defect Type'] = 'CODE Sopra Steria'
			   # print (def_type_analysis['Defect Type'][i])
		
            
			       
def_type_analysis = def_type_analysis.groupby('Defect Type').count()

	# Select only those defect type where count is > 20
def_type_analysis = def_type_analysis[def_type_analysis['Count'] > 20]
After_analysis=def_type_analysis.sort_values(['Count'])

Pareto_analysis(Before_analysis,"Reasons for defects - Before analysis")

Pareto_analysis(After_analysis,"Reasons for defects- After analysis")



