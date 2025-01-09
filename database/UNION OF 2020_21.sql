SELECT * FROM collegedatabase.year2020_21_cap1;

CREATE TABLE new_table AS
-- Rows in year2020_21_cap1 but not in year2020_21_cap2
SELECT
    year2020_21_cap1.Institute_Code,
    year2020_21_cap1.ChoiceCode,
    year2020_21_cap1.CourseName,
    year2020_21_cap1.Exam,
    year2020_21_cap1.CutOffRank AS Cap1CutOffRank,
    year2020_21_cap1.CutOffScore AS Cap1CutOffScore,
    year2020_21_cap2.CutOffRank AS Cap2CutOffRank,
    year2020_21_cap2.CutOffScore AS Cap2CutOffScore
FROM
    year2020_21_cap1
LEFT JOIN
    year2020_21_cap2
ON
    year2020_21_cap1.Institute_Code = year2020_21_cap2.Institute_Code
    AND year2020_21_cap1.ChoiceCode = year2020_21_cap2.ChoiceCode

UNION

-- Rows in year2020_21_cap2 but not in year2020_21_cap1
SELECT
    year2020_21_cap2.Institute_Code,
    year2020_21_cap2.ChoiceCode,
    year2020_21_cap1.CourseName,
    year2020_21_cap1.Exam,
    year2020_21_cap1.CutOffRank AS Cap1CutOffRank,
    year2020_21_cap1.CutOffScore AS Cap1CutOffScore,
    year2020_21_cap2.CutOffRank AS Cap2CutOffRank,
    year2020_21_cap2.CutOffScore AS Cap2CutOffScore
FROM
    year2020_21_cap2
LEFT JOIN
    year2020_21_cap1
ON
    year2020_21_cap1.Institute_Code = year2020_21_cap2.Institute_Code
    AND year2020_21_cap1.ChoiceCode = year2020_21_cap2.ChoiceCode

ORDER BY
    Institute_Code;

