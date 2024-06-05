# Load necessary libraries
library(ggplot2)
library(paletteer)
library(dplyr)

# Create a sample data frame
set.seed(123)
data <- expand.grid(x = LETTERS[1:10], y = LETTERS[1:10])
data$value <- runif(100, min = 0, max = 100)

# Generate the heatmap
ggplot(data, aes(x = x, y = y, fill = value)) +
  geom_tile() +
  scale_fill_paletteer_d("lisa::FridaKahlo") +
  theme_minimal() +
  labs(title = "Heatmap with Frida Kahlo Palette",
       x = "X Axis",
       y = "Y Axis",
       fill = "Value")

# Generate the heatmap
ggplot(data, aes(x = x, y = y, fill = value)) +
  geom_tile() +
  scale_fill_paletteer_d("awtools::gpalette") +
  theme_minimal() +
  labs(title = "Heatmap with GPalette Palette",
       x = "X Axis",
       y = "Y Axis",
       fill = "Value")


# Generate the heatmap
ggplot(data, aes(x = x, y = y, fill = value)) +
  geom_tile() +
  scale_fill_paletteer_c("awtools::gpalette") +
  theme_minimal() +
  labs(title = "Heatmap with GPalette Palette",
       x = "X Axis",
       y = "Y Axis",
       fill = "Value")

# Generate the heatmap
ggplot(data, aes(x = x, y = y, fill = value)) +
  geom_tile() +
  scale_fill_paletteer_c("ggthemes::Orange-Blue Diverging") +
  theme_minimal() +
  labs(title = "Heatmap with Orange-Blue Diverging Palette",
       x = "X Axis",
       y = "Y Axis",
       fill = "Value")
