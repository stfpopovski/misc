function examPrep(input){
    let index = 0;

    let maxPoorGrades = Number(input[index]);
    index++;

    let problemName = input[index];
    index++;

    let problemGrade = Number(input[index]);
    index++;
    
    let poorGradeCounter = 0;
    let gradesCounter = 0;
    let gradesSum = 0;
    let lastProblem = '';

    while (problemName !== "Enough"){
        lastProblem = problemName;
        if (problemGrade <= 4){
            poorGradeCounter++;
        }

        if (poorGradeCounter === maxPoorGrades){
            console.log(`You need a break, ${poorGradeCounter} poor grades.`);
            return;
        }

        gradesCounter++;
        gradesSum += problemGrade;

        problemName = input[index];
        index++;

        problemGrade = Number(input[index]);
        index++;
    }
    let avarageGrade = gradesSum / gradesCounter;

    console.log(`Avarage Score: ${avarageGrade.toFixed(2)}`);
    console.log(`Number of problems: ${gradesCounter}`)
    console.log(`Last Problem: ${lastProblem}`)
}

examPrep (["2",

"Income",

"3",

"Game Info",

"6",

"Best Player",

"4"])