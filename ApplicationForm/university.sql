-- Course table
CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    Title VARCHAR(255),
    Year INT,
    OtherDetails TEXT
);

-- Administrator table
CREATE TABLE Administrator (
    UserID INT PRIMARY KEY,
    Password VARCHAR(255),
    -- Add other administrator details columns as needed
);

-- Applicant table
CREATE TABLE Applicant (
    ApplicantID INT PRIMARY KEY,
    CourseID INT,
    Name VARCHAR(255),
    EntranceExamMarks DECIMAL(5, 2),
    LastUniversityAttended VARCHAR(255),
    PreviousClassMarks DECIMAL(5, 2),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    -- Add other applicant details columns as needed
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
);
