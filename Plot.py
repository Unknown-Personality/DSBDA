import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#line graph
'''x=['Math','English','Hindi']
y=[56,78,90]
y1=[45,98,66]
plt.title('Student Marks')
plt.plot(x,y,marker='o',label='Ram')
plt.plot(x,y1,label='Shyam')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()'''

#bar plot

#Vertical
'''x=[1,2,3,4,5,6,7,8,9,10]
y=[56,78,90,56,78,54,34,40,45,56]
plt.bar(x,y,width=0.2,color=['green','red'])
plt.xlabel('X Values')
plt.ylabel('Y values')
plt.title('Bar Plot')
plt.show()'''
#Horizontal
'''x=[1,2,3,4,5,6,7,8,9,10]
y=[56,78,90,56,78,54,34,40,45,56]
plt.barh(x,y,height=0.2,color=['green','red'])
plt.xlabel('X Values')
plt.ylabel('Y values')
plt.title('Bar Plot')
plt.show()'''

#stacked Bar Graph
'''genres=['Comedy','Action','Romance','Drama','Scifi']
boys=[30,20,40,20,15]
girls=[20,40,20,15,35]
plt.bar(genres,boys,label='BOYS')
plt.bar(genres,girls,bottom=boys,label='GIRLS')
plt.legend()
plt.xlabel('Genres')
plt.ylabel('Number of People')
plt.title('Favourite Movies')
plt.show()'''

#Multiple Bar Graph

'''genres=['Comedy','Action','Romance','Drama','Scifi']
boys=[30,20,40,20,15]
girls=[20,40,20,15,35]

width=0.4
values=np.arange(len(genres))
print(values)

plt.bar(values,boys,width,label="Boys")
plt.bar(values+width,girls,width,label="Girls")

plt.legend()
plt.xticks(values,genres)
plt.xlabel('Genres')
plt.ylabel('Number of People')
plt.title('Favourite Movies')
plt.show()'''

#Pie chart
'''Subject=['Art','Science','Commerce','Other']
per=[25,45,15,15]
explode=(0,0,0.1,0)
plt.pie(per,explode=explode,labels=Subject,autopct='%1.2f%%',shadow=True)
plt.axis('equal')
plt.show()'''


#bar plot using seaborn
'''a=['Sci','Mar','Hindi','English']
b=[20,25,10,40]
sns.barplot(x=a,y=b,width=0.2,color='green')
plt.show()'''

#line plot using seaborn
'''a = ['Sci', 'Mar', 'Hindi', 'English']
b = [20, 25, 10, 40]
sns.pointplot(x=a, y=b, color='blue')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.title('Point Plot of Scores by Subject')
plt.show()'''
