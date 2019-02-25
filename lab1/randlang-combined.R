name <- "Zipf Plots for RandLang1 Corpus"
# pdf("randlang_combined.pdf")
png("randlang_combined.png")

fs <- c(
  "randlang/randlang_len=1000000_sc=0.1.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.2.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.3.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.4.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.5.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.6.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.7.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.8.txt.tsv",
  "randlang/randlang_len=1000000_sc=0.9.txt.tsv"
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
      xlim = c(0,12), ylim = c(0,12),
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
