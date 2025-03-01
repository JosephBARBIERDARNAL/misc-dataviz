from gifing import Gif

path = [f"belgium-unemploymentrate/intermediate/{i}.png" for i in range(1, 57)]

gif = Gif(path, frame_duration=200, n_repeat_last_frame=15)
gif.set_size((1000, 1000), scale=2)
gif.set_background_color("white")
gif.make("belgium-unemploymentrate/build.gif")
