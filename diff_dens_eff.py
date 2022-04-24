# Efficiency Comparision for Carnot Engine with different density

from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import scipy as scp
import scipy.stats as stats

defmfact = 1
eps = 1
rho = [0.01,0.075,0.2,0.3,0.5,0.75,1,1.25,1.5]

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[0]) +' eps '+ str(eps) + ' .txt') as f1: # output file open
        lines1 = f1.readlines()

with open('efficiency with defmfact ' + str(defmfact) + ' rho ' + str(rho[1]) +' eps '+ str(eps) + ' .txt') as f2: # output file open
        lines2 = f2.readlines()

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[2]) +' eps '+ str(eps) + ' .txt') as f3: # output file open
        lines3 = f3.readlines()
        
with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[3]) +' eps '+ str(eps) + ' .txt') as f4: # output file open
        lines4 = f4.readlines()

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[4]) +' eps '+ str(eps) + ' .txt') as f5: # output file open
        lines5 = f5.readlines()
        
with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[5]) +' eps '+ str(eps) + ' .txt') as f6: # output file open
        lines6 = f6.readlines()

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(int(rho[6])) +' eps '+ str(eps) + ' .txt') as f7: # output file open
        lines7 = f7.readlines()

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[7]) +' eps '+ str(eps) + ' .txt') as f8: # output file open
        lines8 = f8.readlines()

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho[8]) +' eps '+ str(eps) + ' .txt') as f9: # output file open
        lines9 = f9.readlines()
        
eff_1 = np.zeros(len(lines1))
count1 = np.zeros(len(lines1)) 

for i in range(0,len(lines1)):
    eff_1[i] = float(lines1[i])
    count1[i] = i+1
    
eff_2 = np.zeros(len(lines2))
count2 = np.zeros(len(lines2)) 

for i in range(0,len(lines2)):
    eff_2[i] = float(lines2[i])
    count2[i] = i+1

eff_3 = np.zeros(len(lines3))
count3 = np.zeros(len(lines3)) 

for i in range(0,len(lines3)):
    eff_3[i] = float(lines3[i])
    count3[i] = i+1

eff_4 = np.zeros(len(lines4))
count4 = np.zeros(len(lines4)) 

for i in range(0,len(lines4)):
    eff_4[i] = float(lines4[i])
    count4[i] = i+1

eff_5 = np.zeros(len(lines5))
count5 = np.zeros(len(lines5)) 

for i in range(0,len(lines5)):
    eff_5[i] = float(lines5[i])
    count5[i] = i+1    

eff_6 = np.zeros(len(lines6))
count6 = np.zeros(len(lines6)) 

for i in range(0,len(lines6)):
    eff_6[i] = float(lines6[i])
    count6[i] = i+1   

eff_7 = np.zeros(len(lines7))
count7 = np.zeros(len(lines7)) 

for i in range(0,len(lines7)):
    eff_7[i] = float(lines7[i])
    count7[i] = i+1
    
eff_8 = np.zeros(len(lines8))
count8 = np.zeros(len(lines8)) 

for i in range(0,len(lines8)):
    eff_8[i] = float(lines8[i])
    count8[i] = i+1
    
eff_9 = np.zeros(len(lines9))
count9 = np.zeros(len(lines9)) 

for i in range(0,len(lines9)):
    eff_9[i] = float(lines9[i])
    count9[i] = i+1

#eff_diff_1 = np.mean(eff_1) - 0.497
#eff_1 = eff_1 - np.ones(len(eff_1))*eff_diff_1

#plt.plot(count1, 0.5*np.ones(len(lines1)),'black', count2, eff_2, count3, eff_3, count4, eff_4)
#plt.legend(['Ideal Efficiency','density = 0.075','density = 0.2','density = 0.3'])#'density = 0.01',
#plt.ylabel('Efficiency')
#plt.xlabel('No. of Cycles')
#plt.title('Efficiency Comparision of Atomistic Carnot Engine with different densities')
#plt.show()
#
#plt.plot(count9, 0.5*np.ones(len(lines9)),'black', count5, eff_5, count6, eff_6, count7, eff_7,count8, eff_8,count9, eff_9)#,count1, eff_1
#plt.legend(['Ideal Efficiency','density = 0.5','density = 0.75','density = 1.0','density = 1.25','density = 1.5'])#'density = 0.01',
#plt.ylabel('Efficiency')
#plt.xlabel('No. of Cycles')
#plt.title('Efficiency Comparision of Atomistic Carnot Engine with different densities')
#plt.show()

pdf_probability_1 = np.zeros(len(eff_1))
pdf_probability_2 = np.zeros(len(eff_2))
pdf_probability_3 = np.zeros(len(eff_3))
pdf_probability_4 = np.zeros(len(eff_4))
pdf_probability_5 = np.zeros(len(eff_5))
pdf_probability_6 = np.zeros(len(eff_6))
pdf_probability_7 = np.zeros(len(eff_7))
pdf_probability_8 = np.zeros(len(eff_7))
pdf_probability_9 = np.zeros(len(eff_7))

eff_mean_1 = st.mean(eff_1)
eff_stddev_1 = st.stdev(eff_1)

eff_mean_2 = st.mean(eff_2)
eff_stddev_2 = st.stdev(eff_2)

eff_mean_3 = st.mean(eff_3)
eff_stddev_3 = st.stdev(eff_3)

eff_mean_4 = st.mean(eff_4)
eff_stddev_4 = st.stdev(eff_4)

eff_mean_5 = st.mean(eff_5)
eff_stddev_5 = st.stdev(eff_5)

eff_mean_6 = st.mean(eff_6)
eff_stddev_6 = st.stdev(eff_6)

eff_mean_7 = st.mean(eff_7)
eff_stddev_7 = st.stdev(eff_7)

eff_mean_8 = st.mean(eff_8)
eff_stddev_8 = st.stdev(eff_8)

eff_mean_9 = st.mean(eff_9)
eff_stddev_9 = st.stdev(eff_9)

for count in range(0,len(eff_1),1):
    pdf_probability_1[count] = stats.norm.pdf(eff_1[count], loc=eff_mean_1, scale=eff_stddev_1)
 
for count in range(0,len(eff_2),1):
    pdf_probability_2[count] = stats.norm.pdf(eff_2[count], loc=eff_mean_2, scale=eff_stddev_2)

for count in range(0,len(eff_3),1):
    pdf_probability_3[count] = stats.norm.pdf(eff_3[count], loc=eff_mean_3, scale=eff_stddev_3)

for count in range(0,len(eff_4),1):
    pdf_probability_4[count] = stats.norm.pdf(eff_4[count], loc=eff_mean_4, scale=eff_stddev_4)        

for count in range(0,len(eff_5),1):
    pdf_probability_5[count] = stats.norm.pdf(eff_5[count], loc=eff_mean_5, scale=eff_stddev_5)

for count in range(0,len(eff_6),1):
    pdf_probability_6[count] = stats.norm.pdf(eff_6[count], loc=eff_mean_6, scale=eff_stddev_6)

for count in range(0,len(eff_7),1):
    pdf_probability_7[count] = stats.norm.pdf(eff_7[count], loc=eff_mean_7, scale=eff_stddev_7)
    
for count in range(0,len(eff_8),1):
    pdf_probability_8[count] = stats.norm.pdf(eff_8[count], loc=eff_mean_8, scale=eff_stddev_8)
    
for count in range(0,len(eff_9),1):
    pdf_probability_9[count] = stats.norm.pdf(eff_9[count], loc=eff_mean_9, scale=eff_stddev_9)

#plt.scatter(eff_2, pdf_probability_2, color = 'orange')
#plt.scatter(eff_3, pdf_probability_3, color = 'yellow')
#plt.scatter(eff_4, pdf_probability_4, color = 'red')
#plt.ylabel('PDF of Calculated Efficiency')
#plt.xlabel('Calculated Efficiency value')
#plt.title('Probability Distribution of Calculated Efficiency for 150 cycle')
#plt.legend(['density = 0.075','density = 0.2','density = 0.3'])
#plt.show()
#
#plt.scatter(eff_5, pdf_probability_5, color = 'black')
#plt.scatter(eff_6, pdf_probability_6, color = 'lawngreen')
#plt.scatter(eff_7, pdf_probability_7, color = 'magenta')
#plt.scatter(eff_8, pdf_probability_8, color = 'peru')
#plt.scatter(eff_9, pdf_probability_9, color = 'brown')
#plt.ylabel('PDF of Calculated Efficiency')
#plt.xlabel('Calculated Efficiency value')
#plt.title('Probability Distribution of Calculated Efficiency for 200 cycles')
#plt.legend(['density = 0.5','density = 0.75','density = 1.0','density = 1.25','density = 1.5'])
#plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Probability Distribution of Calculated Efficiency')
ax1.scatter(eff_2, pdf_probability_2, color = 'orange')
ax1.scatter(eff_3, pdf_probability_3, color = 'yellow')
ax1.scatter(eff_4, pdf_probability_4, color = 'red')
ax1.set(xlabel='Calculated Efficiency value', ylabel='PDF of Calculated Efficiency')
ax1.legend(['density = 0.075','density = 0.2','density = 0.3'])
ax2.scatter(eff_5, pdf_probability_5, color = 'black')
ax2.scatter(eff_6, pdf_probability_6, color = 'lawngreen')
ax2.scatter(eff_7, pdf_probability_7, color = 'magenta')
ax2.scatter(eff_8, pdf_probability_8, color = 'peru')
ax2.scatter(eff_9, pdf_probability_9, color = 'brown')
ax2.set(xlabel='Calculated Efficiency value', ylabel='PDF of Calculated Efficiency')
ax2.legend(['density = 0.5','density = 0.75','density = 1.0','density = 1.25','density = 1.5'])
plt.show()