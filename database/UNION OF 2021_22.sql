CREATE TABLE NEWTABLE1 AS
-- Rows in year2021_22_cap1 but not in year2021_22_cap2
SELECT
    year2021_22_cap1.Institute_Code,
    year2021_22_cap1.ChoiceCode,
    year2021_22_cap1.CourseName,
    year2021_22_cap1.Exam,
    year2021_22_cap1.CutOffRank AS Cap1CutOffRank ,
    year2021_22_cap1.CutOffScore AS Cap1CutOffScore,
    year2021_22_cap2.CutOffRank AS Cap2CutOffRank,
    year2021_22_cap2.CutOffScore AS Cap2CutOffScore
FROM
    year2021_22_cap1
LEFT JOIN
    year2021_22_cap2
ON
    year2021_22_cap1.Institute_Code = year2021_22_cap2.Institute_Code
    AND year2021_22_cap1.ChoiceCode = year2021_22_cap2.ChoiceCode

UNION

-- Rows in year2021_22_cap2 but not in year2021_22_cap1
SELECT
    year2021_22_cap2.Institute_Code,
    year2021_22_cap2.ChoiceCode,
    year2021_22_cap1.CourseName,
    year2021_22_cap1.Exam,
    year2021_22_cap1.CutOffRank AS Cap1CutOffRank,
    year2021_22_cap1.CutOffScore AS Cap1CutOffScore,
    year2021_22_cap2.CutOffRank AS Cap2CutOffRank,
    year2021_22_cap2.CutOffScore AS Cap2CutOffScore
FROM
    year2021_22_cap2
LEFT JOIN
    year2021_22_cap1
ON
    year2021_22_cap1.Institute_Code = year2021_22_cap2.Institute_Code
    AND year2021_22_cap1.ChoiceCode = year2021_22_cap2.ChoiceCode

ORDER BY
    Institute_Code;











