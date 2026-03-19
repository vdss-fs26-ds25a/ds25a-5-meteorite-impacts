# Load the meteorite landings data
df <- read.csv("Meteorite_Landings.csv", check.names = FALSE)

df[df$reclat == 0 & df$reclong == 0, ]

# Select rows where both latitude and longitude are 0
df_no_zero <- df[df$reclat != 0 & df$reclong != 0, ]

head(df_no_zero)

head(df_no_zero[, -1])

write.csv(df_no_zero, "df_no_zero.csv", row.names = FALSE)
