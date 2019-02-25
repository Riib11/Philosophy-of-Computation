name <- "Zipf Plots for RandLang2 Corpus"
# pdf("randenlang_combined.pdf")
png("randenlang_combined.png")

fs <- c(
  "randenlang/randenlang_len=100000_sc=0.1.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.2.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.3.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.4.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.5.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.6.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.7.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.8.txt.tsv",
  "randenlang/randenlang_len=100000_sc=0.9.txt.tsv"
)

i <- 1
for (f in fs) {
  data = read.table(file = f, sep = '\t', header = FALSE)
  rank = 1:length(data$V2)

  # first plot
  if (i == 1) {
    plot(
      log(rank),
      log(data$V2),
      xlim = c(0,10), ylim = c(0,10),
      pch = 16, cex = 0.5,
      
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
      pch = 16, cex = 0.5,
    )
  }
  i <- i + 1
}

# legend
# Add a legend
legend(
  "topright", 
  legend = c(
    "sc = 0.1",
    "sc = 0.2",
    "sc = 0.3",
    "sc = 0.4",
    "sc = 0.5",
    "sc = 0.6",
    "sc = 0.7",
    "sc = 0.8",
    "sc = 0.9"
  ), 

  pch = rep(16, 9),
  col = c(1:5),
  bty = "o",
  pt.cex = 1.0,

  text.col = "black", 
  cex = 1.0, 
  horiz = F,
)

dev.off()
