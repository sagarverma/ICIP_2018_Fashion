import sys
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[10,10])

fig, ax = plt.subplots()
ax.grid(True)

X = [3,5,10,20,30,50]

#Y11 = [0.035, 0.04, 0.05, 0.063, 0.072, 0.08]
Y11 = [0.15, 0.43, 0.48, 0.506, 0.51, 0.53]
#Y12 = [0.037, 0.044, 0.051, 0.071, 0.08, 0.12]
#Y13 = [0.04, 0.063, 0.078, 0.104, 0.13, 0.15 ]
#Y14 = [0.042, 0.064, 0.081, 0.111, 0.135, 0.151]
Y14 = [0.3, 0.56, 0.61, 0.67, 0.70, 0.72]
#Y15 = [0.048, 0.08, 0.1, 0.136, 0.15, 0.175 ]
#Y16 = [0.049, 0.08, 0.1, 0.139, 0.152, 0.176]
#Y17 = [0.075, 0.125, 0.15, 0.188, 0.21, 0.225]
#Y18 = [0.063, 0.085, 0.141, 0.25375, 0.322, 0.416]
Y17 = [0.52, 0.68, 0.72, 0.764, 0.78, 0.80]
Y18 = [0.54, 0.69, 0.73, 0.784, 0.81, 0.84]


ax.plot(X, Y11, **dict(marker='o',markersize=6))
#ax.plot(X, Y12,**marker_style)
#ax.plot(X, Y13,**marker_style)
ax.plot(X, Y14, **dict(marker='s',markersize=6))
#ax.plot(X, Y15,**marker_style)
#ax.plot(X, Y16,**marker_style)
ax.plot(X, Y17, **dict(marker='^',markersize=7))
ax.plot(X, Y18, **dict(marker='*',markersize=8))
plt.xlabel('Retrieved Images(k=1,2,3.....50)', fontsize=25)
plt.ylabel('Average accuracy', fontsize=25)
ticklines = ax.get_xticklines() + ax.get_yticklines()
gridlines = ax.get_xgridlines() + ax.get_ygridlines()
ticklabels = ax.get_xticklabels() + ax.get_yticklabels()

for line in ticklines:
    line.set_linewidth(3)

for line in gridlines:
    line.set_linestyle('-.')

for label in ticklabels:
    #label.set_color('r')
    label.set_fontsize(25)

#plt.legend(['WTBI(0.063)', 'FashionNet+100(0.071)', 'FashionNet+500(0.104)', 'DARN(0.111)', 'FashionNet + Joints(0.136)', 'FashionNet + Poselets(0.139)', 'FashionNet(0.188)', 'Ours(0.253)'], loc='lower right' )
#plt.legend(['WTBI(0.063)', 'DARN(0.111)', 'FashionNet(0.188)', 'Ours(0.253)'], loc='lower right', fontsize=25)
plt.legend(['WTBI(0.506)', 'DARN(0.67)', 'FashionNet(0.764)', 'Ours(0.784)'], loc='lower right', fontsize=25)

#plt.savefig('Consumer2shop.pdf',format="pdf",transparent=True, bbox_inches='tight', pad_inches=0.05)
plt.savefig('Inshop.pdf',format="pdf",transparent=True, bbox_inches='tight', pad_inches=0.05)