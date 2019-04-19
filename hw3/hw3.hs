import Data.List


-- 1. HOPSCOTCH --
everyNth :: [a] -> Int -> [a]
everyNth xs n = [snd x | x <- (zip [1..] xs), fst x `mod` n == 0]

skips :: [a] -> [[a]]
skips xs = map (everyNth xs) [1..length xs]


-- 2. LOCAL MAXIMA --
localMaxima :: [Integer] -> [Integer]
localMaxima = map (!!1) . filter isLocalMax . tails
	where
		isLocalMax (a:b:c:_) = a < b && b > c
		isLocalMax _ 		 = False


-- 3. HISTOGRAM --
groupSort :: (Eq a, Ord a) => [a] -> [[a]]
groupSort xs = group $ sort xs

countInstance :: (Eq a, Ord a) => [a] -> (a, Int)
countInstance xs = (head xs, length xs)

countInstances :: (Eq a, Ord a) => [a] -> [(a, Int)]
countInstances xs = map countInstance $ groupSort xs

maxInstances :: [Int] -> Int
maxInstances = maximum . map snd . countInstances

spaceOrStar :: [Int] -> Int -> Char
spaceOrStar xs y
	| y `elem` xs = '*'
	| otherwise = ' '

getData :: (Eq a, Ord a) => [a] -> Int -> [a]
getData xs n = [fst x | x <- countInstances xs, snd x >= n]

histRow :: [Int] -> String
histRow xs = map (spaceOrStar xs) [0..9]

buildHist :: [Int] -> String
buildHist xs = intercalate "\n" . map (histRow) $ map (getData xs) . reverse $ [1..maxInstances xs]

histogram :: [Int] -> String
histogram xs = buildHist xs ++ "\n==========\n0123456789\n"
