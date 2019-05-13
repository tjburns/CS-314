library('rjson')

heroes <- fromJSON(file='heroes.json')
View(heroes)
pob <- fromJSON(file='pob_match_data.txt')
View(pob)
pob_match_data <- read.csv("C:/Users/tjbur/Google Drive/College/Spring 2019/CS 314/FINAL/pob_match_data.txt", header=FALSE)
View(pob_match_data)
pob <- fromJSON(file='my_matches.json')
View(pob)

winrate <- table(pob[[1]][["radiant_win"]])
View(winrate)

library(rpart)
library(rpart.plot)


match <- read.csv("C:/Users/tjbur/Google Drive/College/Spring 2019/CS 314/FINAL/kaggledata/match.csv")
View(match)

chat <- read.csv("C:/Users/tjbur/Google Drive/College/Spring 2019/CS 314/FINAL/kaggledata/chat.csv")
View(chat)

radiantWins <- table(match$radiant_win)
barplot(radiantWins, main='Faction Win Rate', xlab = 'Radiant Wins (T/F)', ylab = 'Number of Games')

boxplot(match$duration, main = 'Match Duration', ylab = 'Time (s)')

words <- table(chat$key)
finalWords <- sort(words, decreasing=T)
barplot(head(finalWords, 13), main='Most Frequent All Chat Messages', ylab = 'Frequency', xlab = 'Message Content')