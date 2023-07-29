import numpy as np
import matplotlib as plt 
import streamlit as st

st.title('pressure profile in a reservoir')
st.sidebar.title('inputs')
# taking inputs from slider
k = st.sidebar.slider('perm(mD)', min_value=10, max_value=200, value=100)
mu = st.sidebar.slider('viscosity(cP)', min_value=10, max_value=20, value=11)
q = st.sidebar.slider('flowrate', min_value=100, max_value=800, value=120)

## taking inputs from munber inputs
re= st.sidebar.number_input('outer raduis of reservoir(ft)', min_value=100,max_value=10000,value=4000)
rw= st.sidebar.number_input('wellbore raduis(ft)', min_value=1,max_value=10,value=1)
pe= st.sidebar.number_input('pressure at boundary of reservoir(psi)', min_value=100,max_value=10000,value=4000) 
B =st.sidebar.number_input('formation volume factor(bbl/stb)', min_value=1,max_value=2,value=1)
h= st.sidebar.number_input('net pay thickness of reservoir(ft)', min_value=2,max_value=500,value=30)

# logic
r = np.linspace(rw,re,500)
P = pe - (141.2*q*mu*B*(np.log(re/r))/(k*h))
y_min = P[np.where(r==rw)]

## Button
b= st.button('show pressre profile')

if b:
    plt.style.use('classic')
    plt.figure(figsize =(8,3))
    fig,ax=plt.subplots()
    ax.plot(r,P,linewidth=4)
    ax.grid(True)
    ax.axhline(y_min,linewidth=3, color='red')
    ax.set_xlabel('raduis(feet)')
    ax.set_ylabel('pressure at radius r (PSI)')
    ax.set_title('pressure profile')
    ax.set_ylim(0,5000)
    
    ##plotting the figure
    st.pyplot(fig)
    
    
