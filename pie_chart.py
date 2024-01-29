import matplotlib.pyplot as plt 
cat=['A','B','C','D','E']
val=[20,40,12,23,45]
plt.pie(val,labels=cat,autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()