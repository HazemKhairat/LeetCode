SELECT score,
DENSE_RANK() OVER (ORDER BY score DESC) as Rank
FROM Scores