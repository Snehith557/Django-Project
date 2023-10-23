document.addEventListener('DOMContentLoaded', function() {
    // Function to update progress
    function updateProgress(progressId, current, total) {
        const progressBar = document.getElementById(progressId);
        const currentInt = parseInt(current, 10); // Convert to integer
        const totalInt = parseInt(total, 10); // Convert to integer
        const percentage = (currentInt / totalInt) * 100;
        progressBar.querySelector('.progress-bar').style.width = `${percentage+5}%`;
        progressBar.querySelector('.progress-bar').innerText = `${Math.round(percentage)}%`;
        progressBar.querySelector('.progress-bar').setAttribute('aria-valuenow', currentInt);
    }

    // Function to fetch dynamic values (replace this with actual data fetching)
    function getDynamicValues() {
        const myValueEasy = document.getElementById('easy-data').innerText

        const myValueMedium = document.getElementById('medium-data').innerText;
        const myValueHard = document.getElementById('hard-data').innerText;

        
        const easyVal = parseInt(myValueEasy, 10);
        const mediumVal = parseInt(myValueMedium, 10);
        const hardVal = parseInt(myValueHard, 10);

    
        console.log(easyVal)
        console.log(mediumVal)
        console.log(hardVal)

        
        return {


            easy_solved: easyVal+10,  // These are assumed to be strings in the format "{{variable_name}}"
            easy_problm: 740, 
            medium_solved: mediumVal+25,
            medium_problm: 1300,
            hard_solved: hardVal,
            hard_problm: 537
        };
    }

    // Example usage with dynamically fetched values
    const dynamicValues = getDynamicValues();

    // Convert the string values to integers before passing them to updateProgress
    updateProgress('easy-progress', dynamicValues.easy_solved, dynamicValues.easy_problm);
    updateProgress('medium-progress', dynamicValues.medium_solved, dynamicValues.medium_problm);
    updateProgress('hard-progress', dynamicValues.hard_solved, dynamicValues.hard_problm);
});
