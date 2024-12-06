import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin
import matplotlib.animation as animation
from pyfonts import load_font

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
L = L1 + L2  # maximal length of the combined pendulum
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
t_stop = 30  # how many seconds to simulate
history_len = 500  # how many trajectory points to display
fade_segments = 30  # Number of fading segments


def derivs(t, state):
    dydx = np.zeros_like(state)

    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1 + M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = (
        M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
        + M2 * G * sin(state[2]) * cos(delta)
        + M2 * L2 * state[3] * state[3] * sin(delta)
        - (M1 + M2) * G * sin(state[0])
    ) / den1

    dydx[2] = state[3]

    den2 = (L2 / L1) * den1
    dydx[3] = (
        -M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
        + (M1 + M2) * G * sin(state[0]) * cos(delta)
        - (M1 + M2) * L1 * state[1] * state[1] * sin(delta)
        - (M1 + M2) * G * sin(state[2])
    ) / den2

    return dydx


dt = 0.01
t = np.arange(0, t_stop, dt)

th1 = 100.0
w1 = 0.0
th2 = -5.0
w2 = 0.0

state = np.radians([th1, w1, th2, w2])

y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt

x1 = L1 * sin(y[:, 0])
y1 = -L1 * cos(y[:, 0])

x2 = L2 * sin(y[:, 2]) + x1
y2 = -L2 * cos(y[:, 2]) + y1

fig = plt.figure(figsize=(4, 4), dpi=300)
fig.set_facecolor("#000000")
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.0))
ax.set_facecolor("#000000")
ax.set_aspect("equal")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_xticks([])
ax.set_yticks([])
ax.spines[["top", "right", "left", "bottom"]].set(color="white")


font = load_font(
    "https://github.com/coreyhu/Urbanist/blob/main/fonts/ttf/Urbanist-Light.ttf?raw=true"
)
fontbold = load_font(
    "https://github.com/coreyhu/Urbanist/blob/main/fonts/ttf/Urbanist-Bold.ttf?raw=true"
)

fig.text(
    x=0.9,
    y=0.07,
    s="made with @matplotlib",
    size=7,
    font=fontbold,
    color="#f6f6f6",
    ha="right",
    alpha=0.8,
)

(line,) = ax.plot(
    [],
    [],
    "o-",
    lw=3,
    color="#264653",
    markerfacecolor="#2a9d8f",
    markersize=8,
    zorder=20,
)
time_template = "%.1fs"
time_text = ax.text(
    0.05, 0.9, "", transform=ax.transAxes, fontsize=12, color="#ffffff", font=font
)

trace_lines = [
    ax.plot([], [], "-", lw=1.5, color="#e76f51", alpha=(j + 1) / fade_segments)[0]
    for j in range(fade_segments)
]


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)

    for j, trace_line in enumerate(trace_lines):
        start_idx = max(0, i - history_len + j * history_len // fade_segments)
        end_idx = max(0, i - history_len + (j + 1) * history_len // fade_segments)
        trace_line.set_data(x2[start_idx:end_idx], y2[start_idx:end_idx])

    time_text.set_text(time_template % (i * dt))
    return [line, time_text] + trace_lines


ani = animation.FuncAnimation(fig, animate, len(y), interval=dt * 1000, blit=True)
ani.save("pendulum.mp4")
