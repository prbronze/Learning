import numpy as np
import matplotlib.pyplot as plt

def integra(): 
  
  Rm  =  10;  # 10 MOhm
  Ie  =  2;   # 2 nA
  V   = -68 ; # -70mV
  El  = -68 ; # -70mV
  tau =  10 ; # 10ms
   
  tmax = 100; # 100 ms
  dt =   0.1; # 0.1 ms
 
  vThresh = -54; # mV
  vReset  = -80; # mV
 
  tList = np.arange(0,tmax,dt);
  vList = tList * 0;  
 
  I1 = 0
  I2 = 100
  iList = np.zeros(round(I1/dt))
  iList = np.append(iList, np.ones(round((I2-I1)/dt))*Ie )
  iList = np.append(iList, np.zeros(round((tmax-I2)/dt)) )
  freq = 200
  freqz = 0
  

  '''Note que será precisa executar a função
  diversas vezes para cada Ie e tirar a
  médias das frequências do neurônio integra-e-dispara.
 
  #Abaixo temos uma passgem. Agora precisamos criar
  um for loop para mais passagens calculando
  média e std a cada iteração para criar um grafico
  com barras de stderror/std para cada ponto'''

  t = []
  for i in range(0,100):

    for g in range(0,120,5): #até 120nA com rampas de 5 em 5 
        Ie = g
        for step in range(len(tList)):
          Is = 0
          if np.random.rand() < freq*dt/1000:
            Is = Ie
          vList[step] = V
          V = V + dt/tau*(El-V+Rm*Is)
          if V > vThresh:
            vList[step] = 0
            V = vReset
            freqz +=1
        t = np.append(t,freqz)
  
  #print(t[:20])
  #print(t[300:320])       
  #print(t[-20:])
  #t = t.reshape(100,15)
  #print(t[0,:])  
 
  md_freq = t.mean(axis=0)
  std_freq =t.std(axis=0) 
  #plt.plot(tList, vList);
  #plt.savefig('plot.png');
 
  #adicionar os std em yerr
  plt.errorbar(len(range(0,120,5)),md_freq,yerr=std_freq);
  plt.show()


  #falta fazer a média e o std da matriz

# Script ==================================
integra()