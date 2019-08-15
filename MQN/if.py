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
  conta_freq = 0
  

  '''Note que será precisa executar a função diversas vezes para cada
  valor de Ie e tirar a média das frequências do neurônio integra-e-dispara.
 
  Realizamos 50 loops com a corrente variando entre 1 e 251 nA passos de 10.
  Armazenamos em t e então calculamos mean e std para cada valor de Ie.
  Um gráfico de Ie x frequência média de disparos é plotar com o respectivo
  Erro Padrão da Média.
  '''

  t = []
  for i in range(0,50):
    
    for g in range(1,251,10): #até 120nA com rampas de 5 em 5 
      Ie = g
      for step in range(len(tList)):
        Is = 0
        if np.random.rand() < freq*dt/1000:
          Is = Ie
        vList[step] = V
        V = V + dt/tau*((El-V)+Rm*Is)
        if V > vThresh:
          vList[step] = 0
          V = vReset
          conta_freq +=1
      t = np.append(t,conta_freq)
      conta_freq = 0
  

  t = t.reshape(50,25)
  md_freq = t.mean(axis=0)
  std_freq = t.std(axis=0)
  print(md_freq) 
  print(std_freq)

  #plotar os disparos para cada uma das correntes
  #plt.plot(tList, vList);
  #plt.savefig('plot.png');
 
  plt.errorbar(range(1,251,10),md_freq,yerr=std_freq);
  plt.show()

# Script ==================================
integra()