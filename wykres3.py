import matplotlib.pyplot as plt
import mpld3

labels = ['Jabłka', "Banany", "Winogrona", 'Pomarańcze']
sizes = [30, 25, 20, 45]
colors = ['red', 'blue', 'purple', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=90, explode=(0.1, 0, 0, 0),
        autopct='%1.1f%%')  # 34.5%

plt.title('Wykres kołowy')
plt.axis('equal')
html = mpld3.fig_to_html(plt.gcf())
plt.show()

with open('pie.html', 'w') as f:
    f.write(html)
