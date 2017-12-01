import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

# Set up figure and image grid
fig = plt.figure(figsize=(9.75, 3))

grid = ImageGrid(fig, 111,          # as in plt.subplot(111)
                 nrows_ncols=(3,3),
                 axes_pad=0.15,
                 share_all=True,
                 add_all=True,
                 cbar_location="bottom",
                 cbar_mode="single",
                 cbar_size="7%",
                 cbar_pad=0.15,
                 )

# Add data to image grid
for i, ax in enumerate(grid):
    if i ==0 :
        im = ax.imshow(np.random.random((10,10))*100, vmin=0, vmax=100)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        # im.axis('off')
    else:
        im = ax.imshow(np.random.random((10, 10))/2, vmin=0, vmax=1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        # im.axis('off')

# Colorbar
ax.cax.colorbar(im)
ax.cax.toggle_label(True)

#plt.tight_layout()    # Works, but may still require rect paramater to keep colorbar labels visible
plt.show()