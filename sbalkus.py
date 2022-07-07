import seaborn as sns
import matplotlib.font_manager as fm

# import font
fm.fontManager.addfont(r"C:\Users\salba\AppData\Local\Microsoft\Windows\Fonts\Abel.ttf")


# Set up global color palettes
palette_ordered = [
          "#002e5c", #navy
          "#4e7647", #olive
          "#ffa600", #orange
          "#00aaf5", #sky
          "#d1d1d1" #silver
        ]

palette_sbalkus_ordered_dark = [
  "#000332", #navy
  "#234A1E", #olive
  "#C67700", #orange
  "#007BC2", #sky
  "#A0A0A0" #silver
]

palette_unordered = [
          "#002e5c", #navy
          "#ffa600", #orange
          "#4e7647", #olive
          "#00aaf5", #sky
          "#d1d1d1" #silver
        ]

palette_sbalkus_unordered_dark = [
  "#000332", #navy
  "#C67700", #orange
  "#007BC2", #sky
  "#234A1E", #olive
  "#A0A0A0" #silver
]


# Create theme for plots
def set_theme_sbalkus(dpi=288, height=8, width=8, palette_ordered=False):
    context = {
     'font.size': 20.0,
     'axes.labelsize': 'medium',
     'axes.titlesize': 'large',
     'xtick.labelsize': 'medium',
     'ytick.labelsize': 'medium',
     'legend.fontsize': 'medium',
     'axes.linewidth': 1,
     'grid.linewidth': 0.8,
     'lines.linewidth': 1.5,
     'lines.markersize': 6.0,
     'patch.linewidth': 1.0,
     'xtick.major.width': 1,
     'ytick.major.width': 1,
     'xtick.minor.width': 0.6,
     'ytick.minor.width': 0.6,
     'xtick.major.size': 3.5,
     'ytick.major.size': 3.5,
     'xtick.minor.size': 2.0,
     'ytick.minor.size': 2.0,
     'legend.title_fontsize': None
    }

    style = {
     'axes.facecolor': 'white',
     'axes.edgecolor': '4d4d4d',
     'axes.grid': False,
     'axes.axisbelow': 'line',
     'axes.labelcolor': 'black',
     'figure.facecolor': 'white',
     'grid.color': '#b0b0b0',
     'grid.linestyle': '-',
     'text.color': 'black',
     'xtick.color': '4d4d4d',
     'ytick.color': '4d4d4d',
     'xtick.direction': 'out',
     'ytick.direction': 'out',
     #'lines.solid_capstyle': <CapStyle.projecting: 'projecting'>,
     'patch.edgecolor': 'black',
     'patch.force_edgecolor': False,
     'image.cmap': 'viridis',
     'font.family': ['sans-serif'],
     'font.sans-serif': ['Abel'],
     'xtick.bottom': True,
     'xtick.top': False,
     'ytick.left': True,
     'ytick.right': False,
     'axes.spines.left': True,
     'axes.spines.bottom': True,
     'axes.spines.right': True,
     'axes.spines.top': True
    }
    if palette_ordered:
        palette = [
          "#002e5c", #navy
          "#4e7647", #olive
          "#ffa600", #orange
          "#00aaf5", #sky
          "#d1d1d1" #silver
        ]
    else: 
        palette = [
          "#002e5c", #navy
          "#ffa600", #orange
          "#4e7647", #olive
          "#00aaf5", #sky
          "#d1d1d1" #silver
        ]

    sns.set_theme(context=context, style=style, palette=palette, font='sans-serif', font_scale=1, color_codes=True, rc={'figure.dpi':dpi, 'savefig.dpi':dpi, 'figure.figsize':(8,8)})