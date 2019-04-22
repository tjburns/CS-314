
import System.IO
import System.Environment
import Data.List
import System.Random
import Control.Monad
import Data.Char
import Data.Typeable


pickWord :: [a] -> IO a
pickWord xs = randomRIO (0, (length xs - 1)) >>= return . (xs !!)

promptLine :: String -> IO String
promptLine prompt = do
	putStr prompt
	getLine

gameLoop :: String -> String -> IO()
gameLoop word guesses = do
	let
		wordWithGuesses = blankOrChar <$> word
		blankOrChar c
			| c `elem` guesses = c
			| otherwise = '_'
	--putStrLn "Word to guess: " ++ wordWithGuesses
	--putStrLn "Guesses: " ++ guesses	
	putStrLn wordWithGuesses

	if word /= wordWithGuesses
		then do
			charGuess <- getLine
			let newGuesses = guesses ++ charGuess
			--recursive loop
			gameLoop word newGuesses
		else putStrLn "You won!"

main :: IO()
main = do
	-- assume first (and only) argument of hw4.hs is the wordlist used for the hangman game
	--args <- getArgs

	-- assume the file with words is understood to be in the working directory AND known by the program prior to running
	contents <- readFile "words.txt"
	let wordList = words contents
	--let wordList = lines contents
	--print wordList

	word <- pickWord wordList
	--putStrLn word
	--putStrLn ("type of word is: " ++ (show (typeOf word)))	

	--let wordGuess = map (\c -> '_') word
	--putStrLn wordGuess

	let guesses = ""
	
	-- enter gameloop with the chosen word and empty guesses string
	gameLoop word guesses

	-- game assumes guesses are input as lowercase characters.
	-- proper input would be a single char
	-- multiple guesses can be inputted as well as repeat guesses with the method used
	-- upon winning a short victory string is printed and the program exits
