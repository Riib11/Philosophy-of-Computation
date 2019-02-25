args <- commandArgs(TRUE)

name <- "Word Lengths in the Bible"
png("word-lengths_bible.png")

data = read.table(file = args[1], sep = "\t", header = FALSE)
hist(data$V1,
  main=name,
  xlab="Word Length (characters)",
  ylab="Number of Words",
  breaks=15,
  xlim=c(1,15)
)


# hist(AirPassengers, 
#      main="Histogram for Air Passengers", 
#      xlab="Passengers", 
#      border="blue", 
#      col="green",
#      xlim=c(100,700),
#      las=1, 
#      breaks=5)
