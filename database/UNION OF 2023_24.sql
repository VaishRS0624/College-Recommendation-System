create table newtable3 as
-- Rows in year2023_24_cap1 but not in year2023_24_cap2 or year2023_24_cap3
SELECT
    year2023_24_cap1.Institute_Code,
    year2023_24_cap1.ChoiceCode,
    year2023_24_cap1.CourseName,
    year2023_24_cap1.Exam,
    year2023_24_cap1.CutOffRank AS Cap1CutOffRank,
    year2023_24_cap1.CutOffScore AS Cap1CutOffScore,
    year2023_24_cap2.CutOffRank AS Cap2CutOffRank,
    year2023_24_cap2.CutOffScore AS Cap2CutOffScore,
    year2023_24_cap3.CutOffRank AS Cap3CutOffRank,
    year2023_24_cap3.CutOffScore AS Cap3CutOffScore
FROM
    year2023_24_cap1
LEFT JOIN
    year2023_24_cap2
ON
    year2023_24_cap1.Institute_Code = year2023_24_cap2.Institute_Code
    AND year2023_24_cap1.ChoiceCode = year2023_24_cap2.ChoiceCode

LEFT JOIN
    year2023_24_cap3
ON
    year2023_24_cap1.Institute_Code = year2023_24_cap3.Institute_Code
    AND year2023_24_cap1.ChoiceCode = year2023_24_cap3.ChoiceCode

UNION

-- Rows in year2023_24_cap2 but not in year2023_24_cap1 or year2023_24_cap3
SELECT
    year2023_24_cap2.Institute_Code,
    year2023_24_cap2.ChoiceCode,
    year2023_24_cap1.CourseName,
    year2023_24_cap1.Exam,
    year2023_24_cap1.CutOffRank AS Cap1CutOffRank,
    year2023_24_cap1.CutOffScore AS Cap1CutOffScore,
    year2023_24_cap2.CutOffRank AS Cap2CutOffRank,
    year2023_24_cap2.CutOffScore AS Cap2CutOffScore,
    year2023_24_cap3.CutOffRank AS Cap3CutOffRank,
    year2023_24_cap3.CutOffScore AS Cap3CutOffScore
FROM
    year2023_24_cap2
LEFT JOIN
    year2023_24_cap1
ON
    year2023_24_cap1.Institute_Code = year2023_24_cap2.Institute_Code
    AND year2023_24_cap1.ChoiceCode = year2023_24_cap2.ChoiceCode

LEFT JOIN
    year2023_24_cap3
ON
    year2023_24_cap2.Institute_Code = year2023_24_cap3.Institute_Code
    AND year2023_24_cap2.ChoiceCode = year2023_24_cap3.ChoiceCode

UNION

-- Rows in year2023_24_cap3 but not in year2023_24_cap1 or year2023_24_cap2
SELECT
    year2023_24_cap3.Institute_Code,
    year2023_24_cap3.ChoiceCode,
    year2023_24_cap1.CourseName,
    year2023_24_cap1.Exam,
    year2023_24_cap1.CutOffRank AS Cap1CutOffRank,
    year2023_24_cap1.CutOffScore AS Cap1CutOffScore,
    year2023_24_cap2.CutOffRank AS Cap2CutOffRank,
    year2023_24_cap2.CutOffScore AS Cap2CutOffScore,
    year2023_24_cap3.CutOffRank AS Cap3CutOffRank,
    year2023_24_cap3.CutOffScore AS Cap3CutOffScore
FROM
    year2023_24_cap3
LEFT JOIN
    year2023_24_cap1
ON
    year2023_24_cap1.Institute_Code = year2023_24_cap3.Institute_Code
    AND year2023_24_cap1.ChoiceCode = year2023_24_cap3.ChoiceCode

LEFT JOIN
    year2023_24_cap2
ON
    year2023_24_cap2.Institute_Code = year2023_24_cap3.Institute_Code
    AND year2023_24_cap2.ChoiceCode = year2023_24_cap3.ChoiceCode

ORDER BY
    Institute_Code;
