import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


def animate(*maps, res=150, interval=50, frames=100, titles=None, vmin=None, vmax=None):
    """Animate several maps side-by-side in a Jupyter notebook."""
    # Let's first render each map over a grid of thetas
    images = []
    thetas = np.linspace(0, 360, frames)
    x, y = np.meshgrid(np.linspace(-1, 1, res), np.linspace(-1, 1, res))
    for map in np.atleast_1d(maps):
        images.append([np.array([map(theta=theta, x=x[j], y=y[j]) 
                       for j in range(res)]) for theta in thetas])
    images = np.array(images)
    nmaps = images.shape[0]
    if titles is not None:
        titles = np.atleast_1d(titles)
    
    # Set up the plots
    fig, axes = plt.subplots(1, nmaps, figsize=(4 * nmaps, 4))
    axes = np.atleast_1d(axes)
    for i, ax in enumerate(axes):
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.axis('off')
        if titles is not None:
            ax.set_title(titles[i], y=1.05, fontsize=16)
    if vmin is None:
        vmin = np.nanmin(images)
    if vmax is None:
        vmax = np.nanmax(images)
    kwargs = dict(origin="lower", extent=(-1, 1, -1, 1), 
                  cmap="plasma", vmin=vmin,
                  vmax=vmax)
    ims = [ax.imshow([[]], **kwargs) for ax in axes]

    # Initializer function
    def init():
        for im in ims:
            im.set_data([[]])
        return ims

    # Function to animate each frame
    def animate(i):
        for j, im in enumerate(ims):
            im.set_data(images[j, i])
        return ims

    # Generate the animation
    ani = FuncAnimation(fig, animate, init_func=init,
                        frames=frames, interval=interval, 
                        blit=False)
    plt.close()
    display(HTML(ani.to_jshtml()))