# 
# makes plot comparing RandLang3 to several real texts
# 

args <- commandArgs(TRUE)

name <- "Zipf Plots for RandLang3 alongside subset of Real-World Corpus"
# pdf("zipf_combined.pdf")
png("randlengths-real.png")

files = c(
  "randlengths/randlengths_len=100000.txt.tsv",
  "corpus/bible.txt.tsv",
  "corpus/en-dict.txt.tsv",
  "corpus/8cc.txt.tsv",
  "corpus/dantes-inferno.txt.tsv"
)

i <- 1
for (f in files) {
  data = read.table(file = f, sep = '\t', header = FALSE)
  rank = 1:length(data$V2)

  # first plot
  if (i == 1) {
    plot(
      log(rank),
      log(data$V2),
      xlim = c(0,12), ylim = c(0,12),
      # pch = 16,
      cex = 1.0,
      
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
    "RandLang3",
    "Bible",
    "Webster's Dictionary",
    "8cc",
    "Dante's Inferno"
  ), 

  pch = c(1,1,1,1,1),
  col = c(1:5),
  pt.cex = 1.0,

  text.col = "black", 
  cex = 1.0, 
  horiz = F,
)

dev.off()
