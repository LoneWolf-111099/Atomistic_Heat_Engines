#====================Stirling Cycle=====================#
# 1. Isochoric Heat Addition
# 2. Isothermal Expansion
# 3. Isochoric Heat Rejection
# 4. Isothermal Compression

#=====================Import==========================#

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

#==================Reading Function===================#

def avoid_space(string):
    
    count = 0;
    num = np.zeros(5);
    
    string_space_split = string.split(" ");
    
    for i in range(0,len(string_space_split),1):
        
        if string_space_split[i] != "" and string_space_split[i] != "\n": 
            
            num[count] = float(string_space_split[i]);
            count+=1;
            if count == 6: break;
    
    return num;

defmfact = 1
rho = 1.5
eps = 1

file_count1 = 1
file_count2 = 200

no_files = file_count2 - file_count1 + 1

#------------------Sterling Engine----------------------#

carnot_eff = np.zeros(no_files)
proposed_eff = np.zeros(no_files)
q_count = np.zeros(no_files)

T1 = 2.0
T2 = 1.0

scount = 0

for q in range(file_count1,file_count2+1):
    
    # isoth_exp_pvte_defmfact_0.5_rho_1_cyc_148_dat.out
    
    with open('se_isoch_heatadd_pvte_defmfact_'+str(defmfact)+'_rho_' + str(rho) +'_eps_'+str(eps)+'_cyc_'+str(q)+'_dat.out') as f1: # output file open
        lines1 = f1.readlines()
    
    with open('se_isoth_exp_pvte_defmfact_'+str(defmfact)+'_rho_' + str(rho) +'_eps_'+str(eps)+'_cyc_'+str(q)+'_dat.out') as f2: # output file open
        lines2 = f2.readlines()
        
    with open('se_isoch_heatsub_pvte_defmfact_'+str(defmfact)+'_rho_' + str(rho)+'_eps_'+str(eps)+'_cyc_'+str(q)+'_dat.out') as f3: # output file open
        lines3 = f3.readlines()
    
    with open('se_isoth_comp_pvte_defmfact_'+str(defmfact)+'_rho_' + str(rho) +'_eps_'+str(eps)+'_cyc_'+str(q)+'_dat.out') as f4: # output file open
        lines4 = f4.readlines()
    
    #===================Initializing Variables=====================#
    
    initial_step = 1
    max_steps1 = len(lines1) - 1
    max_steps2 = len(lines2) - 1
    max_steps3 = len(lines3) - 1
    max_steps4 = len(lines4) - 1
    
    time1 = np.zeros(max_steps1-1)
    p1 = np.zeros(max_steps1-1)
    v1 = np.zeros(max_steps1-1)
    t1 = np.zeros(max_steps1-1)
    e1 = np.zeros(max_steps1-1)
    
    time2 = np.zeros(max_steps2-1)
    p2 = np.zeros(max_steps2-1)
    v2 = np.zeros(max_steps2-1)
    t2 = np.zeros(max_steps2-1)
    e2 = np.zeros(max_steps2-1)
    
    time3 = np.zeros(max_steps3-1)
    p3 = np.zeros(max_steps3-1)
    v3 = np.zeros(max_steps3-1)
    t3 = np.zeros(max_steps3-1)
    e3 = np.zeros(max_steps3-1)
    
    time4 = np.zeros(max_steps4-1)
    p4 = np.zeros(max_steps4-1)
    v4 = np.zeros(max_steps4-1)
    t4 = np.zeros(max_steps4-1)
    e4 = np.zeros(max_steps4-1)
    
    count = 0
    
    #====================Reading File======================#
    
    for i in range(initial_step,max_steps1,1):
    
        fc = avoid_space(lines1[i])
        
        time1[count] = fc[0]
        p1[count] = fc[1]
        v1[count] = fc[2]
        t1[count] = fc[3]
        e1[count] = fc[4]
        
        count+=1
    
    count = 0
    
    for i in range(initial_step,max_steps2,1):
    
        fc = avoid_space(lines2[i])
        
        time2[count] = fc[0]
        p2[count] = fc[1]
        v2[count] = fc[2]
        t2[count] = fc[3]
        e2[count] = fc[4]
        
        count+=1
    
    count = 0
    
    for i in range(initial_step,max_steps3,1):
    
        fc = avoid_space(lines3[i])
        
        time3[count] = fc[0]
        p3[count] = fc[1]
        v3[count] = fc[2]
        t3[count] = fc[3]
        e3[count] = fc[4]
        
        count+=1
    
    count = 0
    
    for i in range(initial_step,max_steps4,1):
    
        fc = avoid_space(lines4[i])
        
        time4[count] = fc[0]
        p4[count] = fc[1]
        v4[count] = fc[2]
        t4[count] = fc[3]
        e4[count] = fc[4]
        
        count+=1
    
    count = 0

    temp1 = np.mean(t2)
    temp2 = np.mean(t4)
    
    work1 = np.trapz(p1,v1)
    work2 = np.trapz(p2,v2)
    work3 = np.trapz(p3,v3)
    work4 = np.trapz(p4,v4)
    
    #print('\n================='+str(q)+' Cycle================\n')
    
    #print('Work done in Isochoric Heat Addition: ' + str(work1))
    #print('Work done in Isothermal Expansion: ' + str(work2))
    #print('Work done in Isochoric Heat Extraction: ' + str(work3))
    #print('Work done in Isothermal Compresssion: ' + str(work4))
    
    tot_work = work1 + work2 + work3 + work4
    
    energy_diff1 = e1[-1] - e1[0]
    energy_diff2 = e2[-1] - e2[0]
    energy_diff3 = e3[-1] - e3[0]
    energy_diff4 = e4[-1] - e4[0]
    
    #print('Energy Difference in Isentropic Compresssion: ' + str(energy_diff1))
    #print('Energy Difference in Isothermal Expansion: ' + str(energy_diff2))
    #print('Energy Difference in Isentropic Expansion: ' + str(energy_diff3))
    #print('Energy Difference in Isothermal Compresssion: ' + str(energy_diff4))
    
    tot_energy_diff = energy_diff1 + energy_diff2 + energy_diff3 + energy_diff4
    
    heat1 = energy_diff1 + work1
    heat2 = energy_diff2 + work2
    heat3 = energy_diff3 + work3
    heat4 = energy_diff4 + work4
    
    #print('Heat Involved in Isentropic Compresssion: ' + str(heat1))
    #print('Heat Involved in Isothermal Expansion: ' + str(heat2))
    #print('Heat Involved in Isentropic Expansion: ' + str(heat3))
    #print('Heat Involved in Isothermal Compresssion: ' + str(heat4))
    
    posititve_heat = heat2 + heat1 + heat3
    
    eff_car = 1 - (temp2/temp1)
    eff_here = tot_work/posititve_heat
    
    carnot_eff[scount] = eff_car
    proposed_eff[scount] = eff_here
    q_count[scount] = q
    
    #print('Total Work done in cycle: ' + str(tot_work))
    #print('Total Energy Difference in cycle: ' + str(tot_energy_diff))
    #print('Posititve Heat provided: ' + str(posititve_heat))
    #
    #print('Sterling Efficiency: ' + str(eff_car))
    #print('Actual Efficiency: ' + '0.5')
    print('Efficiency Here: ' + str(eff_here))
    
    #if q==1 or q==2:
    #    plt.plot(v1,p1,v2,p2,v3,p3,v4,p4)#,v1,tl1,'--k',v2,tl2,'--k',v3,tl3,'--k',v4,tl4,'--k')
    #    plt.legend(['Isentropic Compression','Isothermal Expansion at T = '+str(T1), 'Isentropic Expansion', 'Isothermal Compression at T = '+str(T2)])
    #    plt.ylabel('Pressure in x-direction [LJ Units]')
    #    plt.xlabel('Volume [LJ Units]')
    #    plt.title('PV diagram of of proposed Sterling Engine with defmfact ' + str(defmfact) + ' rho ' +str(rho) +' eps '+ str(eps))
    #    plt.savefig('PV diagram of of proposed Sterling Engine with defmfact ' + str(defmfact) + ' rho ' +str(rho) +' eps '+ str(eps)+' cycle '+ str(q)+'.png', dpi = 500)
    #    #plt.show()
    
    scount+=1

original_stdout = sys.stdout  

with open('efficiency new with defmfact ' + str(defmfact) + ' rho ' + str(rho) +' eps '+ str(eps) + ' .txt', 'w') as f:
    sys.stdout = f
    for i in range(0,len(proposed_eff),1):
        print(str(proposed_eff[i]))
    sys.stdout = original_stdout

#plt.plot(q_count, (1 - (T2/T1))*np.ones(len(q_count)),q_count,proposed_eff)
#plt.legend(['Fixed Ideal Sterling Efficiency','Calculated Efficiency'])
#plt.ylabel('Efficiency')
#plt.xlabel('No. of Cycles')
#plt.title('Cycle Efficiency of Sterling Engine with defmfact ' + str(defmfact) + ' rho ' +str(rho) +' eps '+ str(eps) + ' with ' + str(scount) + ' cycles')
#plt.savefig('Cycle Efficiency of Sterling Engine with defmfact ' + str(defmfact) + ' rho ' +str(rho) +' eps '+ str(eps) + ' with ' + str(scount) + ' cycles' + '.png', dpi = 500)