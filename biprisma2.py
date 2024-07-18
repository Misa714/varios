import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
import ipywidgets as widgets

def fresnel_biprism_pattern(wavelength, d, D, slit_separation, screen_width, num_points):
    x = np.linspace(-screen_width/2, screen_width/2, num_points)
    path_difference = d * x / D
    intensity = (np.cos(2 * np.pi * path_difference / wavelength))**2
    intensity /= np.max(intensity)

    plt.figure(figsize=(10, 4))
    plt.plot(x * 1e3, intensity, 'b-')
    plt.title('Patrón de Interferencia del Biprisma de Fresnel')
    plt.xlabel('Posición en la pantalla (mm)')
    plt.ylabel('Intensidad Normalizada')
    plt.grid(True)
    plt.show()

wavelength_slider = widgets.FloatSlider(value=500e-9, min=400e-9, max=700e-9, step=10e-9, description='Wavelength (m)')
d_slider = widgets.FloatSlider(value=0.5e-3, min=0.1e-3, max=1e-3, step=0.1e-3, description='d (m)')
D_slider = widgets.FloatSlider(value=1, min=0.5, max=2, step=0.1, description='D (m)')
slit_separation_slider = widgets.FloatSlider(value=2e-3, min=0.5e-3, max=5e-3, step=0.1e-3, description='Slit Separation (m)')
screen_width_slider = widgets.FloatSlider(value=0.01, min=0.005, max=0.02, step=0.001, description='Screen Width (m)')
num_points_slider = widgets.IntSlider(value=5000, min=1000, max=10000, step=500, description='Num Points')

interactive_plot = interactive(fresnel_biprism_pattern,
                               wavelength=wavelength_slider,
                               d=d_slider,
                               D=D_slider,
                               slit_separation=slit_separation_slider,
                               screen_width=screen_width_slider,
                               num_points=num_points_slider)

interactive_plot
