#Single Layer of ANN Model
import numpy as np
import matplotlib.pyplot as plt

def step(output):
    if output > 0:
        return 1
    else:
        return 0
input = [(0,0),(0,1),(1,0),(1,1)]
T=[0,1,0,1]
w=[0,1,-1]
LR=1
Loss_final=[]
for epoch in range(25):
    for i in range(4):
        data = input[i]
        c= T[i]
        output=step(w[0]+w[1]*data[0]+w[2]*data[1])
        loss=LR*(c-output)
        if loss !=0:
            w[0]+=loss*1
            w[1]+=loss*data[0]
            w[2]+=loss*data[1]
        Loss_final.append({'epoch':epoch,'input':data,'loss':loss})
epochs=[key['epoch']for key in Loss_final]
losses=[key['loss']for key in Loss_final]


plt.plot(epochs,losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over Epochs')
plt.show()
