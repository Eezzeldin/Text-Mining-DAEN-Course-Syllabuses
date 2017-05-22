#https://www.linkedin.com/pulse/text-mining-word-cloud-fundamentals-r-rohan-chikorde

#install.packages("tm") # for text mining
install.packages("SnowballC") # for text stemming
#install.packages("wordcloud") # word-cloud generator
install.packages("RColorBrewer") # color palettes

library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

filePath <- "Keywords.txt"
text <- readLines(filePath)
# Load the data as a corpus
docs <- Corpus(VectorSource(text))

toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")

# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))
# Remove numbers
#docs <- tm_map(docs, removeNumbers)
# Remove english common stopwords
docs <- tm_map(docs, removeWords, stopwords("english"))
# Remove your own stop word
# specify your stopwords as a character vector

nowords = c("offered" , "may" , "repeated" , "credit" , "course", "computer","systems","students","introduces","notes","credits","teaches","covers","volgenau","learning","problems","within","will","include","including","basic","use","program")
docs <- tm_map(docs, removeWords, nowords)
# Remove punctuations
docs <- tm_map(docs, removePunctuation)
# Eliminate extra white spaces
docs <- tm_map(docs, stripWhitespace)

# Text stemming
# docs <- tm_map(docs, stemDocument)

dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 100)

set.seed(1234)
quartz()
wordcloud(words = d$word, freq = d$freq, min.freq = 3,
          max.words=1000, random.order=FALSE, rot.per=0.55,
          colors=brewer.pal(8, "Dark2"))



findFreqTerms(dtm, lowfreq = 10)
findAssocs(dtm, terms = c("data","statistics"), corlimit = 0.3)

#quartz()
barplot(d[1:10,]$freq, las = 2, names.arg = d[1:10,]$word,
        col ="lightblue", main ="Most frequent words", 
        ylab = "Word frequencies")
