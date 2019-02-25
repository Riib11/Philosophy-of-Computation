args <- commandArgs(TRUE)

name <- "Zipf Plots for Real-World Corpus"
# pdf("zipf_combined.pdf")
png("zipf_combined.png")

i <- 1
for (f in args){
  data = read.table(file = f, sep = '\t', header = FALSE)
  rank = 1:length(data$V2)

  # first plot
  if (i == 1) {
    plot(
      log(rank),
      log(data$V2),
      xlim = c(0,12), ylim = c(0,12),
      # pch = 16,
      cex = 0.5,
      
      main = name,
      xlab = "Log(Rank)",
      ylab = "Log(Frequency)"
    )
  }
  # subsequent plots
  else {
    points(
      log(rank),
      log(data$V2),
      col = i,
      # pch = 16,
      cex = 0.5,
    )
  }
  i <- i + 1
}

# legend
legend(
  "topright", 
  legend = c(
    "8cc",
    "Bible",
    "Dante's Inferno",
    "Webster English Dictionary",
    "Euclid's Elements",
    "Geonames: AF",
    "Melville's Moby Dick",
    "patentsample",
    "US Cities (short)"
  ), 

  pch = c(1,1,1,1,1,1,1,1,1),
  col = c(1:9),
  pt.cex = 1.0,

  text.col = "black", 
  cex = 1.0, 
  horiz = F,
)

dev.off()
